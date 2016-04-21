# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_auto_20151008_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='endorser',
            field=models.ManyToManyField(related_name='projects_endorsed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='mentors',
            field=models.ManyToManyField(related_name='projects_mentored', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='students',
            field=models.ManyToManyField(related_name='projects_assigned', to=settings.AUTH_USER_MODEL),
        ),
    ]
