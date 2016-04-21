# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Course List', max_length=50)),
                ('course_wide_list', models.BooleanField(default=False, verbose_name=b'Course Wide List')),
                ('project_proposal', models.BooleanField(default=False, verbose_name=b'Project proposal')),
                ('project_assignment', models.BooleanField(default=False, verbose_name=b'Project Assignment')),
                ('projects_per_year', models.IntegerField(default=1, verbose_name=b'Number of Projects per Year')),
                ('project_visibility', models.BooleanField(default=False, verbose_name=b'Project Visibility')),
                ('group', models.ForeignKey(to='auth.Group')),
            ],
            options={
                'verbose_name': 'People List',
                'verbose_name_plural': 'People Lists',
            },
        ),
    ]
