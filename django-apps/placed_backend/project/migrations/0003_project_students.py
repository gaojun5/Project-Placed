# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0002_project_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='students',
            field=models.ManyToManyField(related_name='projects_assigned', to=settings.AUTH_USER_MODEL),
        ),
    ]
