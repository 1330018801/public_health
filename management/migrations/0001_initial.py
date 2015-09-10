# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('ehr', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminNav',
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
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(null=True)),
                ('enabled', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50, null=True)),
                ('level', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DocNav',
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
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GroupProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(null=True)),
                ('enabled', models.IntegerField(default=1)),
                ('is_staff', models.BooleanField(default=None)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RectificationApply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('apply_time', models.DateTimeField(auto_now_add=True)),
                ('finance_opinion', models.IntegerField()),
                ('finance_opinion_time', models.DateTimeField(null=True)),
                ('health_opinion', models.IntegerField()),
                ('health_opinion_time', models.IntegerField(null=True)),
                ('apply_status', models.IntegerField()),
                ('finish_time', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(null=True)),
                ('enabled', models.IntegerField(default=1)),
                ('id', models.CharField(max_length=12, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('level', models.IntegerField()),
                ('ehr_no', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(null=True)),
                ('enabled', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('gender', models.IntegerField(verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(0, b'\xe5\xa5\xb3'), (1, b'\xe7\x94\xb7'), (2, b'\xe6\x9c\xaa\xe7\x9f\xa5')])),
                ('nation', models.CharField(max_length=10, verbose_name=b'\xe6\xb0\x91\xe6\x97\x8f')),
                ('birthday', models.DateField(verbose_name=b'\xe5\x87\xba\xe7\x94\x9f\xe6\x97\xa5\xe6\x9c\x9f')),
                ('address', models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xae\xb6\xe5\xba\xad\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('ehr_no', models.CharField(max_length=17, null=True, verbose_name=b'\xe5\x81\xa5\xe5\xba\xb7\xe6\xa1\xa3\xe6\xa1\x88\xe7\xbc\x96\xe5\x8f\xb7')),
                ('identity', models.CharField(max_length=30, unique=True, null=True, verbose_name=b'\xe8\xba\xab\xe4\xbb\xbd\xe8\xaf\x81\xe5\x8f\xb7\xe7\xa0\x81')),
                ('mobile', models.CharField(max_length=11, null=True, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81', blank=True)),
                ('email', models.EmailField(max_length=75, null=True, verbose_name=b'\xe7\x94\xb5\xe5\xad\x90\xe9\x82\xae\xe7\xae\xb1', blank=True)),
                ('diabetes', models.IntegerField(default=0, verbose_name=b'\xe7\xb3\x96\xe5\xb0\xbf\xe7\x97\x85\xe6\x82\xa3\xe8\x80\x85')),
                ('hypertension', models.IntegerField(default=0, verbose_name=b'\xe9\xab\x98\xe8\xa1\x80\xe5\x8e\x8b\xe6\x82\xa3\xe8\x80\x85')),
                ('psychiatric', models.IntegerField(default=0, verbose_name=b'\xe9\x87\x8d\xe7\x97\x87\xe7\xb2\xbe\xe7\xa5\x9e\xe7\x97\x85\xe6\x82\xa3\xe8\x80\x85')),
                ('pregnant', models.IntegerField(default=0, verbose_name=b'\xe5\xad\x95\xe4\xba\xa7\xe5\xa6\x87')),
                ('create_by', models.ForeignKey(related_query_name=b'created_resident', related_name='created_residents', to=settings.AUTH_USER_MODEL, null=True)),
                ('family', models.ForeignKey(related_query_name=b'members', related_name='members', blank=True, to='management.Family', null=True)),
                ('personal_info_table', models.OneToOneField(null=True, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe5\x9f\xba\xe6\x9c\xac\xe4\xbf\xa1\xe6\x81\xaf\xe8\xa1\xa8', to='ehr.PersonalInfo')),
                ('psychiatric_info_table', models.OneToOneField(null=True, verbose_name=b'\xe9\x87\x8d\xe6\x80\xa7\xe7\xb2\xbe\xe7\xa5\x9e\xe7\x96\xbe\xe7\x97\x85\xe6\x82\xa3\xe8\x80\x85\xe4\xbf\xa1\xe6\x81\xaf\xe8\xa1\xa8', to='ehr.PsychiatricInfo')),
                ('town', models.ForeignKey(related_query_name=b'town_resident', related_name='town_residents', verbose_name=b'\xe6\x89\x80\xe5\x9c\xa8\xe4\xb9\xa1\xe9\x95\x87', to='management.Region', null=True)),
                ('update_by', models.ForeignKey(related_query_name=b'updated_resident', related_name='updated_residents', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(null=True)),
                ('enabled', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=10, null=True)),
                ('price', models.FloatField(null=True)),
                ('real_weight', models.FloatField(null=True)),
                ('should_weight', models.FloatField(null=True)),
                ('level', models.IntegerField()),
                ('alias', models.CharField(max_length=50, null=True)),
                ('code', models.CharField(max_length=6, null=True)),
                ('create_by', models.ForeignKey(related_query_name=b'created_service', related_name='created_services', to=settings.AUTH_USER_MODEL, null=True)),
                ('service_group', models.ForeignKey(related_query_name=b'group_item', related_name='group_items', to='management.Service', null=True)),
                ('service_type', models.ForeignKey(related_query_name=b'service_item', related_name='service_items', to='management.Service', null=True)),
                ('update_by', models.ForeignKey(related_query_name=b'updated_service', related_name='updated_services', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['code'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile', models.CharField(max_length=11, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81')),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('next_time_date', models.DateField(verbose_name=b'\xe4\xb8\x8b\xe6\xac\xa1\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x97\xb6\xe9\x97\xb4')),
                ('service_type_name', models.CharField(max_length=100, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\xb1\xbb\xe5\x88\xab')),
                ('service_item_name', models.CharField(max_length=100, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe9\xa1\xb9\xe7\x9b\xae')),
                ('template_id', models.CharField(max_length=30, verbose_name=b'\xe6\xa8\xa1\xe6\x9d\xbfID')),
                ('status', models.IntegerField(verbose_name=b'\xe7\x9f\xad\xe4\xbf\xa1\xe7\x8a\xb6\xe6\x80\x81')),
                ('message', models.CharField(max_length=300, null=True, verbose_name=b'\xe6\xb6\x88\xe6\x81\xaf\xe5\x86\x85\xe5\xae\xb9/\xe9\x94\x99\xe8\xaf\xaf\xe6\x8f\x90\xe7\xa4\xba')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SmsTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_time', models.DateField(verbose_name=b'\xe4\xb8\x8b\xe6\xac\xa1\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x97\xb6\xe9\x97\xb4')),
                ('status', models.IntegerField(verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81')),
                ('message', models.CharField(max_length=300, null=True)),
                ('create_by', models.ForeignKey(related_query_name=b'created_sms_time', related_name='created_sms_times', to=settings.AUTH_USER_MODEL, null=True)),
                ('service_item', models.ForeignKey(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe9\xa1\xb9\xe7\x9b\xae', to='management.Service')),
                ('service_type', models.ForeignKey(related_query_name=b'sms_service_item', related_name='sms_service_items', verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe7\xb1\xbb\xe5\x88\xab', to='management.Service')),
                ('update_by', models.ForeignKey(related_query_name=b'updated_sms_time', related_name='updated_sms_times', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SvcNav',
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
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(null=True)),
                ('enabled', models.IntegerField(default=1)),
                ('department', models.CharField(max_length=20, null=True, verbose_name=b'\xe7\xa7\x91\xe5\xae\xa4')),
                ('position', models.CharField(max_length=20, null=True, verbose_name=b'\xe5\xb2\x97\xe4\xbd\x8d')),
                ('authorized_services', models.ManyToManyField(related_query_name=b'authorized_user', related_name='authorized_users', null=True, to='management.Service')),
                ('clinic', models.ForeignKey(related_query_name=b'user', related_name='users', verbose_name=b'\xe5\x8d\xab\xe7\x94\x9f\xe9\x99\xa2/\xe5\x8d\xab\xe7\x94\x9f\xe5\xae\xa4', to='management.Clinic', null=True)),
                ('create_by', models.ForeignKey(related_query_name=b'created_user_profile', related_name='created_user_profiles', to=settings.AUTH_USER_MODEL, null=True)),
                ('resident', models.OneToOneField(null=True, to='management.Resident')),
                ('role', models.ForeignKey(related_query_name=b'user', related_name='users', verbose_name=b'\xe8\xa7\x92\xe8\x89\xb2', to='auth.Group')),
                ('update_by', models.ForeignKey(related_query_name=b'updated_user_profile', related_name='updated_user_profiles', to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_label', models.CharField(max_length=50)),
                ('model_name', models.CharField(max_length=50)),
                ('group_item_id', models.IntegerField(null=True)),
                ('item_id', models.IntegerField(null=True)),
                ('service_item_alias', models.CharField(max_length=50, null=True)),
                ('evaluation', models.IntegerField(default=3)),
                ('status', models.IntegerField(default=3)),
                ('begin_time', models.DateTimeField(auto_now_add=True)),
                ('submit_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.FloatField(null=True, verbose_name=django.contrib.auth.models.User)),
                ('provider', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('resident', models.ForeignKey(to='management.Resident')),
                ('service_item', models.ForeignKey(to='management.Service')),
            ],
            options={
                'ordering': ['-submit_time'],
            },
            bases=(models.Model,),
        ),
    ]
