# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_module', '0004_auto_20150922_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodule',
            name='other',
            field=models.TextField(null=True, verbose_name=b'Other'),
        ),
    ]
