# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0009_project_validate'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='favourite',
            field=models.ManyToManyField(related_name='favourite_projects', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='endorser',
            field=models.ManyToManyField(related_name='projects_endorsed', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='mentors',
            field=models.ManyToManyField(related_name='projects_mentored', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='students',
            field=models.ManyToManyField(related_name='projects_assigned', null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
