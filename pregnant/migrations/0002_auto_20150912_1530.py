# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pregnant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aftercare2',
            name='guide',
        ),
        migrations.DeleteModel(
            name='Aftercare2',
        ),
        migrations.RemoveField(
            model_name='aftercare3',
            name='guide',
        ),
        migrations.DeleteModel(
            name='Aftercare3',
        ),
        migrations.RemoveField(
            model_name='aftercare4',
            name='guide',
        ),
        migrations.DeleteModel(
            name='Aftercare4',
        ),
        migrations.RemoveField(
            model_name='aftercare5',
            name='guide',
        ),
        migrations.DeleteModel(
            name='Aftercare5',
        ),
        migrations.DeleteModel(
            name='AlanineAminotransferase',
        ),
        migrations.DeleteModel(
            name='BloodRoutineTest',
        ),
        migrations.DeleteModel(
            name='BloodType',
        ),
        migrations.DeleteModel(
            name='BloodUreaNitrogen',
        ),
        migrations.DeleteModel(
            name='GlutamicOxalaceticTransaminase',
        ),
        migrations.DeleteModel(
            name='HepatitisBFiveItem',
        ),
        migrations.DeleteModel(
            name='SerumCreatinine',
        ),
        migrations.DeleteModel(
            name='TotalBilirubin',
        ),
        migrations.DeleteModel(
            name='UrineRoutineTest',
        ),
    ]
