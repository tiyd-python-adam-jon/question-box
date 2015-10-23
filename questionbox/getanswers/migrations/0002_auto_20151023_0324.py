# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getanswers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='asker',
            field=models.ForeignKey(null=True, blank=True, to='getanswers.Profile'),
        ),
    ]
