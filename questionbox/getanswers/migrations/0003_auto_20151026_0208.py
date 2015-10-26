# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getanswers', '0002_auto_20151025_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='asker',
            field=models.ForeignKey(to='getanswers.Profile', default=1),
            preserve_default=False,
        ),
    ]
