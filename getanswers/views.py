from datetime import datetime  # , timedelta
from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse
from django.shortcuts import redirect  # , render, get_object_or_404
from django.utils.timezone import make_aware
# from django.db.models import Count
# from django.views import generic
from .forms import QuestionForm
from .models import Tag


@login_required
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.asker = request.user.profile
            for t in request.POST['taglist'].split(','):
                tag = Tag(ttext=t.strip())
                tag.save()
                question.tags.add(tag)
                
            question.timestamp = make_aware(datetime.now())
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
