# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20150916_1053'),
        ('ehr', '0003_auto_20150913_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodyexam',
            name='resident',
            field=models.ForeignKey(related_name='body_exam', blank=True, to='management.Resident', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='resident',
            field=models.OneToOneField(related_name='personal_info_table', null=True, to='management.Resident'),
            preserve_default=True,
        ),
    ]
