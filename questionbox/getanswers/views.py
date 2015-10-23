from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login   # , logout
from .models import Profile, Tag
# from datetime import datetime  # , timedelta
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render  # , get_object_or_404
from django.utils.timezone import make_aware
# from django.db.models import Count
# from django.views import generic
from .forms import QuestionForm
# Create your views here.


class UserCreateView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/register'  # TODO: change to question creation?

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
def question_page(request):
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
            # question.asker = request.user.profile
            question.save()
            for t in request.POST['taglist'].split(sep=','):
                tag = Tag(ttext=t.strip())
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
