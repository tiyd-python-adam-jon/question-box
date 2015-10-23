from django.conf.urls import url
from . import views as ga_views


urlpatterns = [
    url(r'^questions/add$',
        ga_views.add_question, name='add_question'),

    url(r'^questions/$', ga_views.question_page, name='question_page'),

    url(r'^questions/(?P<pk>\d+)/answers/add$',
        ga_views.add_answer, name='add_answer'),

    url(r'^questions/answers/$', ga_views.answer_page, name='answer_page'),
]
