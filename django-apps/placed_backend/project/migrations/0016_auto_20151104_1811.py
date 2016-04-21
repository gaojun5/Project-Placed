# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_project_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='company_video',
        ),
    ]
