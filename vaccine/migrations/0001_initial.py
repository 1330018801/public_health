# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visit_date', models.DateField(max_length=10, verbose_name=b'\xe6\x8e\xa5\xe7\xa7\x8d\xe6\x97\xa5\xe6\x9c\x9f')),
                ('vaccinate_position', models.CharField(max_length=100, verbose_name=b'\xe6\x8e\xa5\xe7\xa7\x8d\xe9\x83\xa8\xe4\xbd\x8d')),
                ('batch_number', models.CharField(max_length=100, verbose_name=b'\xe7\x96\xab\xe8\x8b\x97\xe6\x89\xb9\xe5\x8f\xb7')),
                ('remarks', models.CharField(max_length=200, null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True)),
                ('doctor_signature', models.CharField(max_length=20, verbose_name=b'\xe5\x8c\xbb\xe7\x94\x9f\xe7\xad\xbe\xe5\x90\x8d')),
                ('next_vaccinate_date', models.DateField(max_length=15, null=True, verbose_name=b'\xe4\xb8\x8b\xe6\xac\xa1\xe6\x8e\xa5\xe7\xa7\x8d\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('vaccine', models.ForeignKey(verbose_name=b'\xe7\x96\xab\xe8\x8b\x97\xe4\xb8\x8e\xe5\x89\x82\xe6\xac\xa1', to='management.Service')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VaccineCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ehr_village_no', models.CharField(max_length=3, verbose_name=b'\xe5\x81\xa5\xe5\xba\xb7\xe6\xa1\xa3\xe6\xa1\x88\xe7\xbc\x96\xe7\xa0\x81\xe4\xb8\xad\xe6\x9d\x91\xef\xbc\x88\xe7\xa4\xbe\xe5\x8c\xba\xef\xbc\x89\xe5\xaf\xb9\xe5\xba\x94\xe7\x9a\x843\xe4\xbd\x8d\xe7\xbc\x96\xe7\xa0\x81')),
                ('ehr_unique_no', models.CharField(max_length=5, verbose_name=b'\xe5\x81\xa5\xe5\xba\xb7\xe6\xa1\xa3\xe6\xa1\x88\xe7\xbc\x96\xe7\xa0\x81\xe4\xb8\xad\xe6\x9c\x80\xe5\x90\x8e5\xe4\xbd\x8d\xe7\xbc\x96\xe7\xa0\x81')),
                ('gender', models.CharField(max_length=20, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[('\u7537', '\u7537'), ('\u5973', '\u5973')])),
                ('birth_date', models.DateField(max_length=10, verbose_name=b'\xe5\x87\xba\xe7\x94\x9f\xe6\x97\xa5\xe6\x9c\x9f')),
                ('guardian_name', models.CharField(max_length=20, verbose_name=b'\xe7\x9b\x91\xe6\x8a\xa4\xe4\xba\xba\xe5\xa7\x93\xe5\x90\x8d')),
                ('relation_to_child', models.CharField(max_length=10, verbose_name=b'\xe4\xb8\x8e\xe5\x84\xbf\xe7\xab\xa5\xe5\x85\xb3\xe7\xb3\xbb')),
                ('contact_number', models.CharField(max_length=11, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe7\x94\xb5\xe8\xaf\x9d')),
                ('home_county', models.CharField(default=b'\xe4\xb8\x89\xe6\xb2\xb3\xe5\xb8\x82', max_length=20, verbose_name=b'\xe6\x88\xb7\xe7\xb1\x8d\xe5\x9c\xb0\xe5\x9d\x80/\xe5\x8e\xbf\xef\xbc\x88\xe5\x8c\xba\xef\xbc\x89')),
                ('register_local', models.BooleanField(default=False, verbose_name=b'\xe6\x9c\xac\xe5\x9c\xb0\xe6\x88\xb7\xe7\xb1\x8d')),
                ('register_province', models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x88\xb7\xe7\xb1\x8d\xe5\x9c\xb0\xe5\x9d\x80/\xe7\x9c\x81\xef\xbc\x88\xe5\xb8\x82\xe3\x80\x81\xe8\x87\xaa\xe6\xb2\xbb\xe5\x8c\xba\xef\xbc\x89')),
                ('register_city', models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x88\xb7\xe7\xb1\x8d\xe5\x9c\xb0\xe5\x9d\x80/\xe5\xb8\x82')),
                ('register_county', models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x88\xb7\xe7\xb1\x8d\xe5\x9c\xb0\xe5\x9d\x80/\xe5\x8e\xbf\xef\xbc\x88\xe5\x8c\xba\xef\xbc\x89')),
                ('register_town', models.CharField(max_length=20, null=True, verbose_name=b'\xe6\x88\xb7\xe7\xb1\x8d\xe5\x9c\xb0\xe5\x9d\x80/\xe4\xb9\xa1\xe9\x95\x87\xef\xbc\x88\xe8\xa1\x97\xe9\x81\x93\xef\xbc\x89')),
                ('immigrate_time', models.DateField(max_length=10, null=True, verbose_name=b'\xe8\xbf\x81\xe5\x85\xa5\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('emigrate_time', models.DateField(max_length=10, null=True, verbose_name=b'\xe8\xbf\x81\xe5\x87\xba\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('emigrate_reason', models.CharField(max_length=300, null=True, verbose_name=b'\xe8\xbf\x81\xe5\x87\xba\xe5\x8e\x9f\xe5\x9b\xa0', blank=True)),
                ('vaccine_abnormal_reaction_history', models.CharField(max_length=300, verbose_name=b'\xe7\x96\xab\xe8\x8b\x97\xe5\xbc\x82\xe5\xb8\xb8\xe5\x8f\x8d\xe5\xba\x94\xe5\x8f\xb2')),
                ('vaccinate_taboo', models.CharField(max_length=300, verbose_name=b'\xe6\x8e\xa5\xe7\xa7\x8d\xe7\xa6\x81\xe5\xbf\x8c')),
                ('infection_history', models.CharField(max_length=300, verbose_name=b'\xe4\xbc\xa0\xe6\x9f\x93\xe7\x97\x85\xe5\x8f\xb2')),
                ('found_card_date', models.DateField(max_length=10, verbose_name=b'\xe5\xbb\xba\xe5\x8d\xa1\xe6\x97\xa5\xe6\x9c\x9f')),
                ('found_card_person', models.CharField(max_length=20, verbose_name=b'\xe5\xbb\xba\xe5\x8d\xa1\xe4\xba\xba')),
                ('home_town', models.ForeignKey(related_name='town_vaccine_card', verbose_name=b'\xe5\xae\xb6\xe5\xba\xad\xe5\x9c\xb0\xe5\x9d\x80/\xe4\xb9\xa1\xe9\x95\x87\xef\xbc\x88\xe8\xa1\x97\xe9\x81\x93\xef\xbc\x89', to='management.Region')),
            ],
            options={
                'db_table': 'vaccine_card',
            },
            bases=(models.Model,),
        ),
    ]
