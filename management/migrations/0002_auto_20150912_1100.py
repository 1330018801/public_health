# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vaccine', '0001_initial'),
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='vaccine_card',
            field=models.OneToOneField(null=True, verbose_name=b'\xe9\xa2\x84\xe9\x98\xb2\xe6\x8e\xa5\xe7\xa7\x8d\xe5\x8d\xa1', to='vaccine.VaccineCard'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resident',
            name='village',
            field=models.ForeignKey(related_query_name=b'village_resident', related_name='village_residents', verbose_name=b'\xe6\x89\x80\xe5\x9c\xa8\xe6\x9d\x91\xe5\xba\x84/\xe8\xa1\x97\xe9\x81\x93', to='management.Region', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='region',
            name='create_by',
            field=models.ForeignKey(related_query_name=b'created_region', related_name='created_regions', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='region',
            name='town',
            field=models.ForeignKey(to='management.Region', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='region',
            name='update_by',
            field=models.ForeignKey(related_query_name=b'updated_region', related_name='updated_regions', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rectificationapply',
            name='work_record',
            field=models.ForeignKey(to='management.WorkRecord'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupprofile',
            name='create_by',
            field=models.ForeignKey(related_query_name=b'created_group_profile', related_name='created_group_profiles', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupprofile',
            name='default_services',
            field=models.ManyToManyField(related_query_name=b'authorized_group', related_name='authorized_groups', null=True, to='management.Service'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupprofile',
            name='group',
            field=models.OneToOneField(to='auth.Group'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='groupprofile',
            name='update_by',
            field=models.ForeignKey(related_query_name=b'updated_group_profile', related_name='updated_group_profiles', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clinic',
            name='create_by',
            field=models.ForeignKey(related_query_name=b'created_clinic', related_name='created_clinics', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clinic',
            name='region',
            field=models.ForeignKey(related_query_name=b'clinic', related_name='clinics', to='management.Region', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clinic',
            name='town_clinic',
            field=models.ForeignKey(related_query_name=b'village_clinic', related_name='village_clinics', to='management.Clinic', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clinic',
            name='update_by',
            field=models.ForeignKey(related_query_name=b'updated_clinic', related_name='updated_clinics', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
