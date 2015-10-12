# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ehr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodyexam',
            name='b_ultrasonic',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xe5\xbd\xa9\xe8\xb6\x85', blank=True),
            preserve_default=True,
        ),
    ]
