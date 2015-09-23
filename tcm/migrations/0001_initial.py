# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aftercare',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visit_date', models.DateField(max_length=15, verbose_name=b'\xe9\x9a\x8f\xe8\xae\xbf\xe6\x97\xa5\xe6\x9c\x9f')),
                ('guide_extra', models.CharField(max_length=100, null=True, verbose_name=b'', blank=True)),
                ('doctor_signature', models.CharField(max_length=30, verbose_name=b'\xe9\x9a\x8f\xe8\xae\xbf\xe5\x8c\xbb\xe7\x94\x9f\xe7\xad\xbe\xe5\x90\x8d')),
                ('next_visit_date', models.DateField(max_length=15, null=True, verbose_name=b'\xe4\xb8\x8b\xe6\xac\xa1\xe9\x9a\x8f\xe8\xae\xbf\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
            ],
            options={
                'db_table': 'tcm_child_aftercare',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TcmChildGuideChoices1',
            fields=[
                ('choice', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('order', models.IntegerField()),
            ],
            options={
                'db_table': 'tcm_child_guide_choice_1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TcmChildGuideChoices2',
            fields=[
                ('choice', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('order', models.IntegerField()),
            ],
            options={
                'db_table': 'tcm_child_guide_choice_2',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TcmChildGuideChoices3',
            fields=[
                ('choice', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('order', models.IntegerField()),
            ],
            options={
                'db_table': 'tcm_child_guide_choice_3',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='aftercare',
            name='guide',
            field=models.ManyToManyField(to='tcm.TcmChildGuideChoices1', null=True, verbose_name=b'\xe6\x8c\x87\xe5\xaf\xbc', blank=True),
            preserve_default=True,
        ),
    ]
