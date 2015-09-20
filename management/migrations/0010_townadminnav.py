# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_remove_adminnav_town_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='TownAdminNav',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('text', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=20, null=True)),
                ('iconCls', models.CharField(max_length=50, null=True)),
                ('url', models.CharField(max_length=50, null=True)),
                ('nid', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
