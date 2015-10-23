# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getanswers', '0002_auto_20151023_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tag',
            field=models.ManyToManyField(blank=True, to='getanswers.Tag', related_name='tags'),
        ),
    ]
