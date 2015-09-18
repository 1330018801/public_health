# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0003_vaccinecard_resident'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccinecard',
            name='resident',
        ),
    ]
