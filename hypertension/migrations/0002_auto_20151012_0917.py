# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hypertension', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aftercare',
            name='sign_extra',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe5\x85\xb6\xe4\xbb\x96', blank=True),
            preserve_default=True,
        ),
    ]
