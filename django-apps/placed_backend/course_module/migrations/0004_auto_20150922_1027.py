# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_module', '0003_auto_20150921_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodule',
            name='Timeline',
            field=models.TextField(null=True, verbose_name=b'Timeline'),
        ),
        migrations.AlterField(
            model_name='coursemodule',
            name='agreements',
            field=models.TextField(null=True, verbose_name=b'Agreements'),
        ),
        migrations.AlterField(
            model_name='coursemodule',
            name='resources',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Resources'),
        ),
    ]
