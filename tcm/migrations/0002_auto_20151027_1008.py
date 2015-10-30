# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tcm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OldIdentify',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('q1', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q2', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q3', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q4', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q5', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q6', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q7', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q8', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q9', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q10', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q11', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q12', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q13', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q14', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q15', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q16', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q17', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q18', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q19', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q20', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q21', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q22', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q23', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q24', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q25', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q26', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q27', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q28', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q29', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q30', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q31', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q32', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('q33', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=b'', choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
                ('constitution_identify_points_qixu', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('constitution_identify_points_yangxu', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('constitution_identify_points_yinxu', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('constitution_identify_points_tanshi', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('constitution_identify_points_shire', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('constitution_identify_points_xueyu', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('constitution_identify_points_qiyu', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('constitution_identify_points_tebing', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('constitution_identify_points_pinghe', models.PositiveSmallIntegerField(null=True, verbose_name=b'', blank=True)),
                ('constitution_identify_yes_trend_qixu', models.CharField(blank=True, max_length=20, null=True, choices=[('\u662f', b'\xe6\x98\xaf'), ('\u503e\u5411\u662f', b'\xe5\x80\xbe\xe5\x90\x91\xe6\x98\xaf')])),
                ('constitution_identify_yes_trend_yangxu', models.CharField(blank=True, max_length=20, null=True, choices=[('\u662f', b'\xe6\x98\xaf'), ('\u503e\u5411\u662f', b'\xe5\x80\xbe\xe5\x90\x91\xe6\x98\xaf')])),
                ('constitution_identify_yes_trend_yinxu', models.CharField(blank=True, max_length=20, null=True, choices=[('\u662f', b'\xe6\x98\xaf'), ('\u503e\u5411\u662f', b'\xe5\x80\xbe\xe5\x90\x91\xe6\x98\xaf')])),
                ('constitution_identify_yes_trend_tanshi', models.CharField(blank=True, max_length=20, null=True, choices=[('\u662f', b'\xe6\x98\xaf'), ('\u503e\u5411\u662f', b'\xe5\x80\xbe\xe5\x90\x91\xe6\x98\xaf')])),
                ('constitution_identify_yes_trend_shire', models.CharField(blank=True, max_length=20, null=True, choices=[('\u662f', b'\xe6\x98\xaf'), ('\u503e\u5411\u662f', b'\xe5\x80\xbe\xe5\x90\x91\xe6\x98\xaf')])),
                ('constitution_identify_yes_trend_xueyu', models.CharField(blank=True, max_length=20, null=True, choices=[('\u662f', b'\xe6\x98\xaf'), ('\u503e\u5411\u662f', b'\xe5\x80\xbe\xe5\x90\x91\xe6\x98\xaf')])),
                ('constitution_identify_yes_trend_qiyu', models.CharField(blank=True, max_length=20, null=True, choices=[('\u662f', b'\xe6\x98\xaf'), ('\u503e\u5411\u662f', b'\xe5\x80\xbe\xe5\x90\x91\xe6\x98\xaf')])),
                ('constitution_identify_yes_trend_tebing', models.CharField(blank=True, max_length=20, null=True, choices=[('\u662f', b'\xe6\x98\xaf'), ('\u503e\u5411\u662f', b'\xe5\x80\xbe\xe5\x90\x91\xe6\x98\xaf')])),
                ('constitution_identify_yes_trend_pinghe', models.CharField(blank=True, max_length=20, null=True, choices=[('\u662f', b'\xe6\x98\xaf'), ('\u57fa\u672c\u662f', b'\xe5\x9f\xba\xe6\x9c\xac\xe6\x98\xaf')])),
                ('health_care_guide_extra_qixu', models.CharField(max_length=200, null=True, blank=True)),
                ('health_care_guide_extra_yangxu', models.CharField(max_length=200, null=True, blank=True)),
                ('health_care_guide_extra_yinxu', models.CharField(max_length=200, null=True, blank=True)),
                ('health_care_guide_extra_tanshi', models.CharField(max_length=200, null=True, blank=True)),
                ('health_care_guide_extra_shire', models.CharField(max_length=200, null=True, blank=True)),
                ('health_care_guide_extra_xueyu', models.CharField(max_length=200, null=True, blank=True)),
                ('health_care_guide_extra_qiyu', models.CharField(max_length=200, null=True, blank=True)),
                ('health_care_guide_extra_tebing', models.CharField(max_length=200, null=True, blank=True)),
                ('health_care_guide_extra_pinghe', models.CharField(max_length=200, null=True, blank=True)),
                ('fill_table_date', models.DateField(null=True, blank=True)),
                ('doctor_signature', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TcmOldIdentifyChoicesPinghe',
            fields=[
                ('choice', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TcmOldIdentifyChoicesQixu',
            fields=[
                ('choice', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TcmOldIdentifyChoicesQiyu',
            fields=[
                ('choice', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TcmOldIdentifyChoicesShire',
            fields=[
                ('choice', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TcmOldIdentifyChoicesTanshi',
            fields=[
                ('choice', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TcmOldIdentifyChoicesTebing',
            fields=[
                ('choice', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TcmOldIdentifyChoicesXueyu',
            fields=[
                ('choice', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TcmOldIdentifyChoicesYangxu',
            fields=[
                ('choice', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TcmOldIdentifyChoicesYinxu',
            fields=[
                ('choice', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('order', models.PositiveSmallIntegerField()),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='oldidentify',
            name='health_care_guide_pinghe',
            field=models.ManyToManyField(to='tcm.TcmOldIdentifyChoicesPinghe', null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='oldidentify',
            name='health_care_guide_qixu',
            field=models.ManyToManyField(to='tcm.TcmOldIdentifyChoicesQixu', null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='oldidentify',
            name='health_care_guide_qiyu',
            field=models.ManyToManyField(to='tcm.TcmOldIdentifyChoicesQiyu', null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='oldidentify',
            name='health_care_guide_shire',
            field=models.ManyToManyField(to='tcm.TcmOldIdentifyChoicesShire', null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='oldidentify',
            name='health_care_guide_tanshi',
            field=models.ManyToManyField(to='tcm.TcmOldIdentifyChoicesTanshi', null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='oldidentify',
            name='health_care_guide_tebing',
            field=models.ManyToManyField(to='tcm.TcmOldIdentifyChoicesTebing', null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='oldidentify',
            name='health_care_guide_xueyu',
            field=models.ManyToManyField(to='tcm.TcmOldIdentifyChoicesXueyu', null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='oldidentify',
            name='health_care_guide_yangxu',
            field=models.ManyToManyField(to='tcm.TcmOldIdentifyChoicesYangxu', null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='oldidentify',
            name='health_care_guide_yinxu',
            field=models.ManyToManyField(to='tcm.TcmOldIdentifyChoicesYinxu', null=True, verbose_name=b'', blank=True),
            preserve_default=True,
        ),
    ]
