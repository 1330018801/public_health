# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diabetes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aftercare1',
            name='symptom',
        ),
        migrations.DeleteModel(
            name='Aftercare1',
        ),
        migrations.RemoveField(
            model_name='aftercare2',
            name='symptom',
        ),
        migrations.DeleteModel(
            name='Aftercare2',
        ),
        migrations.RemoveField(
            model_name='aftercare3',
            name='symptom',
        ),
        migrations.DeleteModel(
            name='Aftercare3',
        ),
        migrations.RemoveField(
            model_name='aftercare4',
            name='symptom',
        ),
        migrations.DeleteModel(
            name='Aftercare4',
        ),
        migrations.RemoveField(
            model_name='aftercare',
            name='sign_blood_pressure',
        ),
        migrations.AddField(
            model_name='aftercare',
            name='sign_dbp',
            field=models.FloatField(default=100, verbose_name=b'\xe8\xa1\x80\xe5\x8e\x8b-\xe8\x88\x92\xe5\xbc\xa0\xe5\x8e\x8b'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aftercare',
            name='sign_sbp',
            field=models.FloatField(default=70, verbose_name=b'\xe8\xa1\x80\xe5\x8e\x8b-\xe6\x94\xb6\xe7\xbc\xa9\xe5\x8e\x8b'),
            preserve_default=False,
        ),
    ]
