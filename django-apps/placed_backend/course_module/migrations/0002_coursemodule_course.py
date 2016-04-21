# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_website_link'),
        ('course_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemodule',
            name='course',
            field=models.ForeignKey(default=1, to='course.Course'),
            preserve_default=False,
        ),
    ]
