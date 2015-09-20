# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_townadminnav'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TownAdminNav',
        ),
    ]
