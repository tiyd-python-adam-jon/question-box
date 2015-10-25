from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login  # , logout
from .models import Profile, Tag, Question, Answer
# from datetime import datetime  # , timedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render, get_object_or_404
# from django.utils.timezone import make_aware
from django.db.models import Count
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

# Create your views here.


class UserCreateView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/'  # TODO: change to question creation?

    def form_valid(self, form):
        new_user = form.save()
        # new_user.save()
        new_profile = Profile(user=new_user)
        new_profile.save()
        user = authenticate(username=new_user.username,
                            password=form.cleaned_data['password1'])
        login(self.request, user)
        return super(UserCreateView, self).form_valid(form)


# Simple page to check add_question
def question_form(request):
    form = QuestionForm()
    return render(request,
                  'getanswers/add_question.html',
                  {'form': form})


# @login_required
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.asker = request.user.profile
            question.asker.points += 5
            question.asker.save()
            question.save()
            for t in request.POST['taglist'].lower().split(sep=','):
                t = t.strip()
                try:
                    tag = Tag.objects.get(ttext=t)
                except:
                    tag = Tag(ttext=t)
                    tag.save()
                question.tag.add(tag)
                question.save()

            messages.add_message(request,
                                 messages.SUCCESS,
                                 'You successfully posted your question')
        else:
            messages.add_message(request,
                                 messages.ERROR,
                                 'Form data invalid, complete required fields')
    else:
        messages.add_message(request,
                             messages.ERROR,
                             'Stop trying to hack this site!')
    return redirect(request.GET['next'])


# @login_required
def add_answer(request, pk):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = get_object_or_404(Question, pk=pk)
            answer.answerer = request.user.profile
            answer.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'You successfully posted your answer')
        else:
            messages.add_message(request,
                                 messages.ERROR,
                                 'Form data invalid, complete required fields')
    else:
        messages.add_message(request,
                             messages.ERROR,
                             'Stop trying to hack this site!')
    return redirect(request.GET['next'])


@login_required
def upvote_answer(request, pk):
    if request.method == 'POST':  # TODO: Make this possible to come in as POST
        answer = get_object_or_404(Answer, pk=request.POST['answerpk'])
        answer.score += 1
        answer.save()
        answer.answerer.points += 10
        answer.answerer.save()
        messages.add_message(request,
                             messages.SUCCESS,
                             'You successfully upvoted that answer')
    else:
        messages.add_message(request,
                             messages.ERROR,
                             'Stop trying to hack this site!')
    return redirect(request.POST['next'])


@login_required
def downvote_answer(request, pk):
    if request.method == 'POST':  # TODO: Make this possible to come in as POST
        answer = get_object_or_404(Answer, pk=request.POST['answerpk'])
        answer.score -= 1
        answer.save()
        answer.answerer.points -= 5
        answer.answerer.save()
        request.user.profile.points -= 1
        request.user.profile.save()
        messages.add_message(request,
                             messages.SUCCESS,
                             'You successfully downvoted that answer')
    else:
        messages.add_message(request,
                             messages.ERROR,
                             'Stop trying to hack this site!')
    return redirect(request.POST['next'])


class QuestionListView(ListView):
    """Used to view a list of questions in reverse chronological order
    Used for home page"""

    template_name = 'getanswers/question_list.html'
    context_object_name = 'questions'
    paginate_by = 10

    def get_queryset(self):
        self.alltags = Tag.objects.annotate(num_qs=Count('questions')).order_by('-num_qs')[:20]
        preload = Question.objects.all()
        return preload.order_by('-timestamp')


class AnswerListView(ListView):
    template_name = 'getanswers/answer_list.html'
    context_object_name = 'answers'
    paginate_by = 10

    def get_queryset(self):
        self.form = AnswerForm()
        self.question = get_object_or_404(Question, pk=self.kwargs['pk'])
        self.alltags = Tag.objects.annotate(num_qs=Count('questions')) \
            .order_by('-num_qs')[:20]
        return self.question.answer_set.all().order_by('-score') \
            .prefetch_related('answerer')


class ProfileDetailView(DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        return context


class ProfileQuestionsView(ListView):
    template_name = 'getanswers/profile_questions.html'
    context_object_name = 'questions'
    paginate_by = 10

    def get_queryset(self):
        self.profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        self.username = self.profile.user
        return self.profile.question_set.all().order_by('-timestamp')


class ProfileAnswersView(ListView):
    template_name = 'getanswers/profile_answers.html'
    context_object_name = 'answers'
    paginate_by = 10

    def get_queryset(self):
        self.profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        self.username = self.profile.user
        return self.profile.answer_set.all().order_by('-timestamp')
