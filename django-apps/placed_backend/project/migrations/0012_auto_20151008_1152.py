# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20151008_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='favourite',
            field=models.ManyToManyField(related_name='favourite_projects', to=settings.AUTH_USER_MODEL),
        ),
    ]
