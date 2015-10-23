from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User)
    points = models.IntegerField(null=True)
    date_created = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.username


class Question(models.Model):
    title = models.CharField(max_length=255)
    qtext = models.TextField()
    asker = models.ForeignKey(Profile)
    tag = models.ManyToManyField('Tag', related_name='tags')
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question)
    answerer = models.ForeignKey(Profile)
    atext = models.TextField()
    score = models.IntegerField()
    timestamp = models.DateTimeField()
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return '{}: {}'.format(self.answerer, self.atext)


class Tag(models.Model):
    ttext = models.CharField(max_length=50)

    def __str__(self):
        return self.ttext


class Vote(models.Model):
    voter = models.ForeignKey(Profile)
    foranswer = models.ForeignKey(Answer)
    vote = models.BooleanField()

    def __str__(self):
        return self.vote

#

#

#

#
