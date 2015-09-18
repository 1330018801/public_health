# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ehr', '0004_auto_20150916_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bodyexam',
            name='resident',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='resident',
        ),
    ]
