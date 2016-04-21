# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_auto_20151008_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='creator',
            field=models.ForeignKey(related_name='projects_created', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
