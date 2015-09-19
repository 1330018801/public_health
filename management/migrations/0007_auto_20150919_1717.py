# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_auto_20150919_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modifyapply',
            name='health_opinion_time',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
