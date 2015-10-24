from django.conf.urls import url
from . import views as ga_views


urlpatterns = [
    url(r'^questions/$',
        ga_views.QuestionListView.as_view(), name='question_list'),

    url(r'^questions/add$',
        ga_views.add_question, name='add_question'),

    url(r'^questions/form$', ga_views.question_form, name='question_form'),

    url(r'^questions/(?P<pk>\d+)/$',
        ga_views.AnswerListView.as_view(), name='answer_list'),

    url(r'^questions/(?P<pk>\d+)/add$',
        ga_views.add_answer, name='add_answer'),

    url(r'^$', ga_views.QuestionListView.as_view(), name='home'),
]
