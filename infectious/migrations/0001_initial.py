# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RiskManagement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('risk_inspection', models.TextField(verbose_name=b'\xe9\xa3\x8e\xe9\x99\xa9\xe6\x8e\x92\xe6\x9f\xa5')),
                ('risk_information', models.TextField(verbose_name=b'\xe9\xa3\x8e\xe9\x99\xa9\xe4\xbf\xa1\xe6\x81\xaf')),
                ('risk_evaluation', models.TextField(verbose_name=b'\xe9\xa3\x8e\xe9\x99\xa9\xe8\xaf\x84\xe4\xbc\xb0')),
                ('contingency_plan', models.TextField(verbose_name=b'\xe5\xba\x94\xe6\x80\xa5\xe9\xa2\x84\xe6\xa1\x88')),
                ('report_time', models.DateTimeField(verbose_name=b'\xe6\x8a\xa5\xe5\x91\x8a\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'risk_management',
            },
            bases=(models.Model,),
        ),
    ]
