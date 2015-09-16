# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_svcnav_classification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resident',
            name='personal_info_table',
        ),
        migrations.RemoveField(
            model_name='resident',
            name='psychiatric_info_table',
        ),
        migrations.RemoveField(
            model_name='resident',
            name='vaccine_card',
        ),
    ]
