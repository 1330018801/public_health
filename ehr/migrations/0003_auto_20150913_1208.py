# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ehr', '0002_auto_20150912_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodyexam',
            name='doctor',
            field=models.CharField(max_length=10, null=True, verbose_name=b'\xe8\xb4\xa3\xe4\xbb\xbb\xe5\x8c\xbb\xe7\x94\x9f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyexam',
            name='visit_date',
            field=models.DateField(null=True, verbose_name=b'\xe4\xbd\x93\xe6\xa3\x80\xe6\x97\xa5\xe6\x9c\x9f', blank=True),
            preserve_default=True,
        ),
    ]
