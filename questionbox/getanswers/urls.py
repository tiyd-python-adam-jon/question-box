from django.conf.urls import url
from . import views as ga_views


urlpatterns = [
    url(r'^questions/add$',
        ga_views.add_question, name='add_question'),

    url(r'^questions/$', ga_views.question_page, name='question_page'),

    url(r'^questions/(?P<pk>\d+)/$',
        ga_views.AnswerListView.as_view(), name='answer_list'),

    url(r'^$', ga_views.QuestionListView.as_view(), name='question_list'),
]
