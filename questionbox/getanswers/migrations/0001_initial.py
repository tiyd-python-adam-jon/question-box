# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('atext', models.TextField()),
                ('score', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('points', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('qtext', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('asker', models.ForeignKey(null=True, to='getanswers.Profile', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('ttext', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('vote', models.BooleanField()),
                ('foranswer', models.ForeignKey(to='getanswers.Answer')),
                ('voter', models.ForeignKey(to='getanswers.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.ManyToManyField(to='getanswers.Tag', related_name='tags'),
        ),
        migrations.AddField(
            model_name='answer',
            name='answerer',
            field=models.ForeignKey(to='getanswers.Profile'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='getanswers.Question'),
        ),
    ]
