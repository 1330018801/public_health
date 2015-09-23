# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('act_time', models.DateTimeField(verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe6\x97\xb6\xe9\x97\xb4')),
                ('scene', models.CharField(max_length=100, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe5\x9c\xb0\xe7\x82\xb9')),
                ('act_type', models.CharField(max_length=100, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe5\xbd\xa2\xe5\xbc\x8f')),
                ('subject', models.CharField(max_length=150, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe4\xb8\xbb\xe9\xa2\x98')),
                ('organizer', models.CharField(max_length=50, verbose_name=b'\xe7\xbb\x84\xe7\xbb\x87\xe8\x80\x85')),
                ('crowd_type', models.CharField(max_length=50, verbose_name=b'\xe6\x8e\xa5\xe5\x8f\x97\xe5\x81\xa5\xe5\xba\xb7\xe6\x95\x99\xe8\x82\xb2\xe4\xba\xba\xe5\x91\x98\xe7\xb1\xbb\xe5\x88\xab')),
                ('crowd_num', models.IntegerField(verbose_name=b'\xe6\x8e\xa5\xe5\x8f\x97\xe5\x81\xa5\xe5\xba\xb7\xe6\x95\x99\xe8\x82\xb2\xe4\xba\xba\xe6\x95\xb0')),
                ('material_type', models.CharField(max_length=50, verbose_name=b'\xe5\x81\xa5\xe5\xba\xb7\xe6\x95\x99\xe8\x82\xb2\xe8\xb5\x84\xe6\x96\x99\xe5\x8f\x91\xe6\x94\xbe\xe7\xa7\x8d\xe7\xb1\xbb')),
                ('material_num', models.IntegerField(verbose_name=b'\xe5\x81\xa5\xe5\xba\xb7\xe6\x95\x99\xe8\x82\xb2\xe8\xb5\x84\xe6\x96\x99\xe5\x8f\x91\xe6\x94\xbe\xe6\x95\xb0\xe9\x87\x8f')),
                ('content', models.CharField(max_length=1000, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe5\x86\x85\xe5\xae\xb9')),
                ('summary', models.CharField(max_length=1000, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe6\x80\xbb\xe7\xbb\x93\xe8\xaf\x84\xe4\xbb\xb7')),
            ],
            options={
                'db_table': 'education_activity',
            },
            bases=(models.Model,),
        ),
    ]
