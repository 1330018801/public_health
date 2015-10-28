# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20151013_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workrecord',
            name='update_by',
            field=models.ForeignKey(related_name='update_records', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
