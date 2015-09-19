# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20150916_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModifyApply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('apply_time', models.DateTimeField(auto_now_add=True)),
                ('finance_opinion', models.IntegerField(default=1)),
                ('finance_opinion_time', models.DateTimeField(null=True)),
                ('health_opinion', models.IntegerField(default=1)),
                ('health_opinion_time', models.IntegerField(null=True)),
                ('apply_status', models.IntegerField()),
                ('finish_time', models.DateTimeField(null=True)),
                ('work_record', models.OneToOneField(related_name='modify_apply', to='management.WorkRecord')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='rectificationapply',
            name='work_record',
        ),
        migrations.DeleteModel(
            name='RectificationApply',
        ),
    ]
