# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getanswers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='tag',
            field=models.ManyToManyField(to='getanswers.Tag', related_name='questions'),
        ),
    ]
