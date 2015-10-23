from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Profile
# Create your views here.


class UserCreateView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/register'  # TODO: change to question creation?

    def form_valid(self, form):
        new_user = form.save()
        new_profile = Profile(user=new_user)
        new_profile.save()
        user = authenticate(username=new_user.username,
                            password=form.cleaned_data['password1'])
        login(self.request, user)
        return super(UserCreateView, self).form_valid(form)
