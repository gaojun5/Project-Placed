# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('project', '0014_project_coordinators'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='company',
            field=models.ForeignKey(default=1, to='company.Company'),
            preserve_default=False,
        ),
    ]
