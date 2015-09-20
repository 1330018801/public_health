# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_delete_townadminnav'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminnav',
            name='town_clinic_admin',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
