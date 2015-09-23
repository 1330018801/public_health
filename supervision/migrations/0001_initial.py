# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('discover_time', models.DateTimeField(verbose_name=b'\xe5\x8f\x91\xe7\x8e\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('info_type', models.CharField(max_length=50, verbose_name=b'\xe4\xbf\xa1\xe6\x81\xaf\xe7\xb1\xbb\xe5\x88\xab')),
                ('info_content', models.TextField(max_length=1000, verbose_name=b'\xe4\xbf\xa1\xe6\x81\xaf\xe5\x86\x85\xe5\xae\xb9')),
                ('report_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x8a\xa5\xe5\x91\x8a\xe6\x97\xb6\xe9\x97\xb4')),
                ('reporter', models.CharField(max_length=50, verbose_name=b'\xe6\x8a\xa5\xe5\x91\x8a\xe4\xba\xba')),
                ('institution', models.ForeignKey(verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84', to='management.Clinic')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place_content', models.TextField(max_length=1000, verbose_name=b'\xe5\xb7\xa1\xe6\x9f\xa5\xe5\x9c\xb0\xe7\x82\xb9\xe4\xb8\x8e\xe5\x86\x85\xe5\xae\xb9')),
                ('main_problem', models.TextField(max_length=2000, verbose_name=b'\xe5\x8f\x91\xe7\x8e\xb0\xe7\x9a\x84\xe4\xb8\xbb\xe8\xa6\x81\xe9\x97\xae\xe9\xa2\x98')),
                ('inspection_date', models.DateField(verbose_name=b'\xe5\xb7\xa1\xe6\x9f\xa5\xe6\x97\xa5\xe6\x9c\x9f')),
                ('inspector', models.CharField(max_length=50, verbose_name=b'\xe5\xb7\xa1\xe6\x9f\xa5\xe4\xba\xba')),
                ('remarks', models.TextField(max_length=1000, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe7\x99\xbb\xe8\xae\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('create_by', models.ForeignKey(verbose_name=b'\xe7\x99\xbb\xe8\xae\xb0\xe4\xba\xba', to=settings.AUTH_USER_MODEL)),
                ('institution', models.ForeignKey(verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84', to='management.Clinic')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
