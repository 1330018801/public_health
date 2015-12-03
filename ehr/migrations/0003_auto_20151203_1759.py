# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ehr', '0002_auto_20151109_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodyexam',
            name='mouth_tooth_decayed_bottomleft',
            field=models.CharField(max_length=10, null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyexam',
            name='mouth_tooth_decayed_bottomright',
            field=models.CharField(max_length=10, null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyexam',
            name='mouth_tooth_decayed_upleft',
            field=models.CharField(max_length=10, null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyexam',
            name='mouth_tooth_decayed_upright',
            field=models.CharField(max_length=10, null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyexam',
            name='mouth_tooth_denture_bottomleft',
            field=models.CharField(max_length=10, null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyexam',
            name='mouth_tooth_denture_bottomright',
            field=models.CharField(max_length=10, null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyexam',
            name='mouth_tooth_denture_upleft',
            field=models.CharField(max_length=10, null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyexam',
            name='mouth_tooth_denture_upright',
            field=models.CharField(max_length=10, null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyexam',
            name='mouth_tooth_missing_bottomleft',
            field=models.CharField(max_length=10, null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyexam',
            name='mouth_tooth_missing_bottomright',
            field=models.CharField(max_length=10, null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyexam',
            name='mouth_tooth_missing_upleft',
            field=models.CharField(max_length=10, null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bodyexam',
            name='mouth_tooth_missing_upright',
            field=models.CharField(max_length=10, null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
    ]
