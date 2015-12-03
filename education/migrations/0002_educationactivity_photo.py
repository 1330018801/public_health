# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationactivity',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'images/%Y%m%d'),
            preserve_default=True,
        ),
    ]
