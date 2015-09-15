# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20150912_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='svcnav',
            name='classification',
            field=models.CharField(default='individual', max_length=20),
            preserve_default=False,
        ),
    ]
