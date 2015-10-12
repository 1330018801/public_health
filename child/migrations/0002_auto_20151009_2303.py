# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aftercare12month',
            name='rickets_sign',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name=b'\xe5\x8f\xaf\xe7\x96\x91\xe4\xbd\x9d\xe5\x81\xbb\xe7\x97\x85\xe4\xbd\x93\xe5\xbe\x81', choices=[('"o"\u578b\u817f', b'"o"\xe5\x9e\x8b\xe8\x85\xbf'), ('"x"\u578b\u817f', b'"x"\xe5\x9e\x8b\xe8\x85\xbf')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aftercare18month',
            name='rickets_sign',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name=b'\xe5\x8f\xaf\xe7\x96\x91\xe4\xbd\x9d\xe5\x81\xbb\xe7\x97\x85\xe4\xbd\x93\xe5\xbe\x81', choices=[('"o"\u578b\u817f', b'"o"\xe5\x9e\x8b\xe8\x85\xbf'), ('"x"\u578b\u817f', b'"x"\xe5\x9e\x8b\xe8\x85\xbf')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aftercare24month',
            name='rickets_sign',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name=b'\xe5\x8f\xaf\xe7\x96\x91\xe4\xbd\x9d\xe5\x81\xbb\xe7\x97\x85\xe4\xbd\x93\xe5\xbe\x81', choices=[('"o"\u578b\u817f', b'"o"\xe5\x9e\x8b\xe8\x85\xbf'), ('"x"\u578b\u817f', b'"x"\xe5\x9e\x8b\xe8\x85\xbf')]),
            preserve_default=True,
        ),
    ]
