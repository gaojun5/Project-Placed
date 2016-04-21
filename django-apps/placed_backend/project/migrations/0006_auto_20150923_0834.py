# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20150922_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='company_video',
            field=models.URLField(null=True, verbose_name=b'Company Video'),
        ),
    ]
