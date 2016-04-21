# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import email_validation.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('email_validation', '0002_auto_20150827_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailvalidation',
            name='group',
            field=models.ForeignKey(default=1, to='auth.Group'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emailvalidation',
            name='code',
            field=models.CharField(default=email_validation.models.default_code, max_length=32, verbose_name=b'code'),
        ),
        migrations.AlterField(
            model_name='emailvalidation',
            name='expires',
            field=models.DateTimeField(default=email_validation.models.default_expires, verbose_name=b'Expires'),
        ),
    ]
