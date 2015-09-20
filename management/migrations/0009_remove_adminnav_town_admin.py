# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_adminnav_town_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminnav',
            name='town_admin',
        ),
    ]
