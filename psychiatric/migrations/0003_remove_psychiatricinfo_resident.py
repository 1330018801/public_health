# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psychiatric', '0002_psychiatricinfo_resident'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='psychiatricinfo',
            name='resident',
        ),
    ]
