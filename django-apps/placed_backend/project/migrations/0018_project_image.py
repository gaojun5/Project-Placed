# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_project_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to=b'project/profile', null=True, verbose_name=b'Project Image'),
        ),
    ]
