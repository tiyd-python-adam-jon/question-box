from django import forms
# from django.contrib.auth.models import User
from getanswers.models import Question


class QuestionForm(forms.ModelForm):
    title = forms.CharField(label='', help_text='', widget=forms.TextInput(
        attrs={'size': '40', 'class': 'form-control',
               'placeholder': 'Question Title (required)'}))
    qtext = forms.CharField(label='', help_text='', widget=forms.Textarea(
        attrs={'cols': 80, 'rows': 12, 'class': 'form-control',
               'placeholder': 'Question Text (required)'}))
    taglist = forms.CharField(label='', help_text='', widget=forms.TextInput(
        attrs={'size': '40', 'class': 'form-control',
               'placeholder': 'Tags'}))

    class Meta:
        model = Question
        fields = ['title', 'qtext', 'taglist']
