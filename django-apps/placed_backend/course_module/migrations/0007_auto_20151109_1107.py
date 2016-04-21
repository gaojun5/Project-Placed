# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_module', '0006_coursemodule_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemodule',
            name='academic_name',
            field=models.CharField(default=b'', max_length=250, verbose_name=b'Academic name'),
        ),
        migrations.AddField(
            model_name='coursemodule',
            name='display_name',
            field=models.CharField(default=b'', max_length=250, verbose_name=b'Display name'),
        ),
        migrations.AlterField(
            model_name='coursemodule',
            name='name',
            field=models.CharField(default=b'Module name', max_length=50),
        ),
    ]
