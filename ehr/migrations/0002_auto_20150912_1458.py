# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ehr', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AlanineAminotransferase',
        ),
        migrations.DeleteModel(
            name='BloodFat',
        ),
        migrations.DeleteModel(
            name='BloodGlucose',
        ),
        migrations.DeleteModel(
            name='BloodRoutineTest',
        ),
        migrations.DeleteModel(
            name='BloodUreaNitrogen',
        ),
        migrations.DeleteModel(
            name='ConstitutionIdentification',
        ),
        migrations.DeleteModel(
            name='Electrocardiogram',
        ),
        migrations.DeleteModel(
            name='GlutamicOxalaceticTransaminase',
        ),
        migrations.DeleteModel(
            name='OldBodyCheck',
        ),
        migrations.DeleteModel(
            name='PhysicalExamination',
        ),
        migrations.DeleteModel(
            name='PsyBodyCheck',
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
