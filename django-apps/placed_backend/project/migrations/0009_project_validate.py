# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20151005_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='validate',
            field=models.BooleanField(default=False, verbose_name=b'Validate'),
        ),
    ]
