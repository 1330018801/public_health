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
                ('visit_date', models.DateField(max_length=10, verbose_name=b'\xe9\x9a\x8f\xe8\xae\xbf\xe6\x97\xa5\xe6\x9c\x9f')),
                ('visit_way', models.CharField(max_length=10, verbose_name=b'\xe9\x9a\x8f\xe8\xae\xbf\xe6\x96\xb9\xe5\xbc\x8f', choices=[('\u95e8\u8bca', b'\xe9\x97\xa8\xe8\xaf\x8a'), ('\u5bb6\u5ead', b'\xe5\xae\xb6\xe5\xba\xad'), ('\u7535\u8bdd', b'\xe7\x94\xb5\xe8\xaf\x9d')])),
                ('symptom_extra', models.TextField(null=True, verbose_name=b'\xe5\x85\xb6\xe4\xbb\x96', blank=True)),
                ('sign_sbp', models.FloatField(verbose_name=b'\xe8\xa1\x80\xe5\x8e\x8b-\xe6\x94\xb6\xe7\xbc\xa9\xe5\x8e\x8b')),
                ('sign_dbp', models.FloatField(verbose_name=b'\xe8\xa1\x80\xe5\x8e\x8b-\xe8\x88\x92\xe5\xbc\xa0\xe5\x8e\x8b')),
                ('sign_weight', models.FloatField(verbose_name=b'\xe4\xbd\x93\xe9\x87\x8d')),
                ('sign_weight_next', models.FloatField(verbose_name=b'')),
                ('sign_bmi', models.FloatField(verbose_name=b'\xe4\xbd\x93\xe8\xb4\xa8\xe6\x8c\x87\xe6\x95\xb0')),
                ('sign_bmi_next', models.FloatField(verbose_name=b'')),
                ('sign_heart_rhythm', models.FloatField(verbose_name=b'\xe5\xbf\x83\xe7\x8e\x87')),
                ('sign_extra', models.CharField(max_length=100, null=True, verbose_name=b'\xe5\x85\xb6\xe4\xbb\x96', blank=True)),
                ('life_style_guide_smoke', models.PositiveSmallIntegerField(verbose_name=b'\xe6\x97\xa5\xe5\x90\xb8\xe7\x83\x9f\xe9\x87\x8f')),
                ('life_style_guide_smoke_next', models.PositiveSmallIntegerField(verbose_name=b'')),
                ('life_style_guide_liquor', models.PositiveSmallIntegerField(verbose_name=b'\xe6\x97\xa5\xe9\xa5\xae\xe9\x85\x92\xe9\x87\x8f')),
                ('life_style_guide_liquor_next', models.PositiveSmallIntegerField(verbose_name=b'')),
                ('life_style_guide_sport1', models.PositiveSmallIntegerField(verbose_name=b'\xe8\xbf\x90\xe5\x8a\xa8')),
                ('life_style_guide_sport2', models.PositiveSmallIntegerField()),
                ('life_style_guide_sport3', models.PositiveSmallIntegerField()),
                ('life_style_guide_sport4', models.PositiveSmallIntegerField()),
                ('life_style_guide_salt', models.CharField(max_length=10, verbose_name=b'\xe6\x91\x84\xe7\x9b\x90\xe6\x83\x85\xe5\x86\xb5', choices=[('\u8f7b', b'\xe8\xbd\xbb'), ('\u4e2d', b'\xe4\xb8\xad'), ('\u91cd', b'\xe9\x87\x8d')])),
                ('life_style_guide_salt_next', models.CharField(max_length=10, choices=[('\u8f7b', b'\xe8\xbd\xbb'), ('\u4e2d', b'\xe4\xb8\xad'), ('\u91cd', b'\xe9\x87\x8d')])),
                ('life_style_guide_mentality', models.CharField(max_length=10, verbose_name=b'\xe5\xbf\x83\xe7\x90\x86\xe8\xb0\x83\xe6\x95\xb4', choices=[('\u826f\u597d', b'\xe8\x89\xaf\xe5\xa5\xbd'), ('\u4e00\u822c', b'\xe4\xb8\x80\xe8\x88\xac'), ('\u5dee', b'\xe5\xb7\xae')])),
                ('life_style_guide_medical_compliance', models.CharField(max_length=10, verbose_name=b'\xe9\x81\xb5\xe5\x8c\xbb\xe8\xa1\x8c\xe4\xb8\xba', choices=[('\u826f\u597d', b'\xe8\x89\xaf\xe5\xa5\xbd'), ('\u4e00\u822c', b'\xe4\xb8\x80\xe8\x88\xac'), ('\u5dee', b'\xe5\xb7\xae')])),
                ('auxiliary_examination', models.TextField(null=True, verbose_name=b'\xe8\xbe\x85\xe5\x8a\xa9\xe6\xa3\x80\xe6\x9f\xa5*', blank=True)),
                ('take_medicine_compliance', models.CharField(max_length=10, verbose_name=b'\xe6\x9c\x8d\xe8\x8d\xaf\xe4\xbe\x9d\xe4\xbb\x8e\xe6\x80\xa7', choices=[('\u89c4\u5f8b', b'\xe8\xa7\x84\xe5\xbe\x8b'), ('\u95f4\u65ad', b'\xe9\x97\xb4\xe6\x96\xad'), ('\u4e0d\u670d\u836f', b'\xe4\xb8\x8d\xe6\x9c\x8d\xe8\x8d\xaf')])),
                ('medicine_untoward_effect', models.CharField(max_length=10, verbose_name=b'\xe8\x8d\xaf\xe7\x89\xa9\xe4\xb8\x8d\xe8\x89\xaf\xe5\x8f\x8d\xe5\xba\x94', choices=[('\u65e0', b'\xe6\x97\xa0'), ('\u6709', b'\xe6\x9c\x89')])),
                ('medicine_untoward_effect_yes', models.CharField(max_length=100, null=True, blank=True)),
                ('visit_classification', models.CharField(max_length=100, verbose_name=b'\xe6\xad\xa4\xe6\xac\xa1\xe9\x9a\x8f\xe8\xae\xbf\xe5\x88\x86\xe7\xb1\xbb', choices=[('\u63a7\u5236\u6ee1\u610f', b'\xe6\x8e\xa7\xe5\x88\xb6\xe6\xbb\xa1\xe6\x84\x8f'), ('\u63a7\u5236\u4e0d\u6ee1\u610f', b'\xe6\x8e\xa7\xe5\x88\xb6\xe4\xb8\x8d\xe6\xbb\xa1\xe6\x84\x8f'), ('\u4e0d\u826f\u53cd\u5e94', b'\xe4\xb8\x8d\xe8\x89\xaf\xe5\x8f\x8d\xe5\xba\x94'), ('\u5e76\u53d1\u75c7', b'\xe5\xb9\xb6\xe5\x8f\x91\xe7\x97\x87')])),
                ('take_medicine_1', models.CharField(max_length=100, null=True, verbose_name=b'\xe8\x8d\xaf\xe7\x89\xa9\xe5\x90\x8d\xe7\xa7\xb01', blank=True)),
                ('take_medicine_1_day', models.PositiveSmallIntegerField(null=True, verbose_name=b'\xe7\x94\xa8\xe6\xb3\x95\xe7\x94\xa8\xe9\x87\x8f', blank=True)),
                ('take_medicine_1_time', models.FloatField(null=True, blank=True)),
                ('take_medicine_2', models.CharField(max_length=100, null=True, verbose_name=b'\xe8\x8d\xaf\xe7\x89\xa9\xe5\x90\x8d\xe7\xa7\xb02', blank=True)),
                ('take_medicine_2_day', models.PositiveSmallIntegerField(null=True, verbose_name=b'\xe7\x94\xa8\xe6\xb3\x95\xe7\x94\xa8\xe9\x87\x8f', blank=True)),
                ('take_medicine_2_time', models.FloatField(null=True, blank=True)),
                ('take_medicine_3', models.CharField(max_length=100, null=True, verbose_name=b'\xe8\x8d\xaf\xe7\x89\xa9\xe5\x90\x8d\xe7\xa7\xb03', blank=True)),
                ('take_medicine_3_day', models.PositiveSmallIntegerField(null=True, verbose_name=b'\xe7\x94\xa8\xe6\xb3\x95\xe7\x94\xa8\xe9\x87\x8f', blank=True)),
                ('take_medicine_3_time', models.FloatField(null=True, blank=True)),
                ('take_medicine_qt', models.CharField(max_length=100, null=True, verbose_name=b'\xe5\x85\xb6\xe4\xbb\x96\xe8\x8d\xaf\xe7\x89\xa9', blank=True)),
                ('take_medicine_qt_day', models.PositiveSmallIntegerField(null=True, verbose_name=b'\xe7\x94\xa8\xe6\xb3\x95\xe7\x94\xa8\xe9\x87\x8f', blank=True)),
                ('take_medicine_qt_time', models.FloatField(null=True, blank=True)),
                ('transfer_treatment_reason', models.CharField(max_length=1000, null=True, verbose_name=b'\xe5\x8e\x9f\xe5\x9b\xa0', blank=True)),
                ('transfer_treatment_institution', models.CharField(max_length=1000, null=True, verbose_name=b'\xe6\x9c\xba\xe6\x9e\x84\xe5\x8f\x8a\xe7\xa7\x91\xe5\xae\xa4', blank=True)),
                ('next_visit_date', models.DateField(verbose_name=b'\xe4\xb8\x8b\xe6\xac\xa1\xe9\x9a\x8f\xe8\xae\xbf\xe6\x97\xa5\xe6\x9c\x9f')),
                ('doctor_signature', models.CharField(max_length=20, verbose_name=b'\xe9\x9a\x8f\xe8\xae\xbf\xe5\x8c\xbb\xe7\x94\x9f\xe7\xad\xbe\xe5\x90\x8d')),
            ],
            options={
                'db_table': 'hypertension_aftercare',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SymptomChoices',
            fields=[
                ('choice', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('order', models.IntegerField()),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='aftercare',
            name='symptom',
            field=models.ManyToManyField(to='hypertension.SymptomChoices', null=True, verbose_name=b'\xe7\x97\x87\xe7\x8a\xb6', blank=True),
            preserve_default=True,
        ),
    ]
