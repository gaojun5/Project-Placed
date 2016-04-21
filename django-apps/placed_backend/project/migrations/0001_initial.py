# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('course_module', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('skill', '0001_initial'),
        ('project_target_device', '0001_initial'),
        ('project_platform', '0001_initial'),
        ('project_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150, verbose_name=b'Title')),
                ('company_video', models.URLField(verbose_name=b'Company Video')),
                ('visibility', models.CharField(default=b'private', max_length=50, verbose_name=b'Visibility', choices=[(b'public', b'Public'), (b'private', b'Private')])),
                ('desired_start_date', models.DateField(verbose_name=b'Desired Start Date')),
                ('desired_end_date', models.DateField(verbose_name=b'Desired End Date')),
                ('brief', models.TextField(verbose_name=b'Brief')),
                ('scope', models.TextField(verbose_name=b'Scope')),
                ('resources_provided', models.TextField(verbose_name=b'Resources provided')),
                ('student_needed', models.IntegerField(verbose_name=b'Students needed')),
                ('terms_agreement', models.TextField(verbose_name=b'Terms Agreement')),
                ('ip_agreement', models.TextField(verbose_name=b'IP Agreement')),
                ('data', models.ManyToManyField(to='project_data.ProjectData')),
                ('endorser', models.ManyToManyField(related_name='projects_endorsed', to=settings.AUTH_USER_MODEL)),
                ('mentors', models.ManyToManyField(related_name='projects_mentored', to=settings.AUTH_USER_MODEL)),
                ('module', models.ForeignKey(to='course_module.CourseModule')),
                ('platform', models.ManyToManyField(to='project_platform.ProjectPlatform')),
                ('skills_needed', models.ManyToManyField(related_name='projects_need_it', to='skill.Skill')),
                ('skills_practised', models.ManyToManyField(related_name='projects_practise_it', to='skill.Skill')),
                ('target_device', models.ManyToManyField(to='project_target_device.ProjectTargetDevice')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
