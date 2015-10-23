from datetime import datetime  # , timedelta
from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render  # , get_object_or_404
from django.utils.timezone import make_aware
# from django.db.models import Count
# from django.views import generic
from .forms import QuestionForm, AnswerForm
from .models import Tag, Question


# Simple page to check add_question
def question_page(request):
    '''This is for testing purposes only'''
    form = QuestionForm()
    return render(request,
                  'getanswers/add_question.html',
                  {'form': form})

# Simple page to check add_answer
def answer_page(request):
    '''This is for testing purposes only'''
    form = AnswerForm()
    question = Question.objects.first()
    return render(request,
                  'getanswers/add_answer.html',
                  {'question': question,
                   'form': form})


# @login_required
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            # question.asker = request.user.profile
            question.timestamp = make_aware(datetime.now())
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


# @login_required
def add_answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            # TODO: put question=xx in query string
            answer.question = request.GET['question']
            # answer.asker = request.user.profile
            answer.timestamp = make_aware(datetime.now())
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
