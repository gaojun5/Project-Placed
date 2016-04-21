# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people_list', '0004_peoplelist_send_invitations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peoplelist',
            name='module',
            field=models.ForeignKey(to='course_module.CourseModule', null=True),
        ),
    ]
