# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adboard',
            name='healtheducate_ptr',
        ),
        migrations.DeleteModel(
            name='AdBoard',
        ),
        migrations.RemoveField(
            model_name='adboardmaintenance',
            name='healtheducate_ptr',
        ),
        migrations.DeleteModel(
            name='AdBoardMaintenance',
        ),
        migrations.RemoveField(
            model_name='adboardupdate',
            name='healtheducate_ptr',
        ),
        migrations.DeleteModel(
            name='AdBoardUpdate',
        ),
        migrations.RemoveField(
            model_name='adbook',
            name='healtheducate_ptr',
        ),
        migrations.DeleteModel(
            name='AdBook',
        ),
        migrations.RemoveField(
            model_name='adbooklet',
            name='healtheducate_ptr',
        ),
        migrations.DeleteModel(
            name='AdBooklet',
        ),
        migrations.RemoveField(
            model_name='adpage',
            name='healtheducate_ptr',
        ),
        migrations.DeleteModel(
            name='AdPage',
        ),
        migrations.RemoveField(
            model_name='healtheducationwebsite',
            name='healtheducate_ptr',
        ),
        migrations.DeleteModel(
            name='HealthEducationWebsite',
        ),
        migrations.RemoveField(
            model_name='healthknowledgelecture',
            name='healtheducate_ptr',
        ),
        migrations.DeleteModel(
            name='HealthKnowledgeLecture',
        ),
        migrations.RemoveField(
            model_name='publichealthconsultation',
            name='healtheducate_ptr',
        ),
        migrations.DeleteModel(
            name='PublicHealthConsultation',
        ),
        migrations.RemoveField(
            model_name='shelf',
            name='healtheducate_ptr',
        ),
        migrations.DeleteModel(
            name='Shelf',
        ),
        migrations.RemoveField(
            model_name='video',
            name='healtheducate_ptr',
        ),
        migrations.DeleteModel(
            name='HealthEducate',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
