# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getanswers', '0003_auto_20151023_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tag',
            field=models.ManyToManyField(related_name='tags', to='getanswers.Tag'),
        ),
    ]
