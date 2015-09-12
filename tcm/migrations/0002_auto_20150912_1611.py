# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tcm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aftercare12month',
            name='guide',
        ),
        migrations.DeleteModel(
            name='Aftercare12Month',
        ),
        migrations.RemoveField(
            model_name='aftercare18month',
            name='guide',
        ),
        migrations.DeleteModel(
            name='Aftercare18Month',
        ),
        migrations.RemoveField(
            model_name='aftercare24month',
            name='guide',
        ),
        migrations.DeleteModel(
            name='Aftercare24Month',
        ),
        migrations.RemoveField(
            model_name='aftercare30month',
            name='guide',
        ),
        migrations.DeleteModel(
            name='Aftercare30Month',
        ),
        migrations.RemoveField(
            model_name='aftercare3year',
            name='guide',
        ),
        migrations.DeleteModel(
            name='Aftercare3Year',
        ),
        migrations.RemoveField(
            model_name='aftercare6month',
            name='guide',
        ),
        migrations.DeleteModel(
            name='Aftercare6Month',
        ),
    ]
