# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_module', '0002_coursemodule_course'),
        ('people_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='peoplelist',
            name='module',
            field=models.ForeignKey(default=1, to='course_module.CourseModule'),
            preserve_default=False,
        ),
    ]
