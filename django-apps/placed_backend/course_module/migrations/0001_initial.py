# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('exemplar_project_proposal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('skill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Module default', max_length=50)),
                ('project_scope', models.TextField(verbose_name=b'Project Scope')),
                ('students_per_project', models.IntegerField(verbose_name=b'Number students per Project')),
                ('Timeline', models.TextField(verbose_name=b'Timeline')),
                ('resources', models.CharField(max_length=50, verbose_name=b'Resources')),
                ('other', models.TextField(verbose_name=b'Other')),
                ('agreements', models.TextField(verbose_name=b'Agreements')),
                ('exemplar_project_proposal', models.ForeignKey(to='exemplar_project_proposal.ExemplarProjectProposal')),
                ('project_coordinator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('skills', models.ManyToManyField(to='skill.Skill')),
            ],
            options={
                'verbose_name': 'Course Module',
                'verbose_name_plural': 'Course Modules',
            },
        ),
    ]
