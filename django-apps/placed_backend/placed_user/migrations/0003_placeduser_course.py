# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_website_link'),
        ('placed_user', '0002_placeduser_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeduser',
            name='course',
            field=models.ForeignKey(to='course.Course', null=True),
        ),
    ]
