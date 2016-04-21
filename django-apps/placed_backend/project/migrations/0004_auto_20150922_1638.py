# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_students'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='skills_practised',
            new_name='skills_practiced',
        ),
    ]
