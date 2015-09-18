# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20150916_1053'),
        ('vaccine', '0002_auto_20150912_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccinecard',
            name='resident',
            field=models.OneToOneField(related_name='vaccine_cared', null=True, to='management.Resident'),
            preserve_default=True,
        ),
    ]
