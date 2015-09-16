# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psychiatric', '0003_remove_psychiatricinfo_resident'),
        ('ehr', '0005_auto_20150916_1357'),
        ('vaccine', '0004_remove_vaccinecard_resident'),
        ('management', '0004_auto_20150916_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='personal_info_table',
            field=models.OneToOneField(null=True, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe5\x9f\xba\xe6\x9c\xac\xe4\xbf\xa1\xe6\x81\xaf\xe8\xa1\xa8', to='ehr.PersonalInfo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resident',
            name='psychiatric_info_table',
            field=models.OneToOneField(null=True, verbose_name=b'\xe9\x87\x8d\xe6\x80\xa7\xe7\xb2\xbe\xe7\xa5\x9e\xe7\x96\xbe\xe7\x97\x85\xe6\x82\xa3\xe8\x80\x85\xe4\xbf\xa1\xe6\x81\xaf\xe8\xa1\xa8', to='psychiatric.PsychiatricInfo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='resident',
            name='vaccine_card',
            field=models.OneToOneField(null=True, verbose_name=b'\xe9\xa2\x84\xe9\x98\xb2\xe6\x8e\xa5\xe7\xa7\x8d\xe5\x8d\xa1', to='vaccine.VaccineCard'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workrecord',
            name='app_label',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workrecord',
            name='model_name',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='workrecord',
            name='service_item',
            field=models.ForeignKey(to='management.Service', null=True),
            preserve_default=True,
        ),
    ]
