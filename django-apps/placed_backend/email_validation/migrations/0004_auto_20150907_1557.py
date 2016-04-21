# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('email_validation', '0003_auto_20150831_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailvalidation',
            name='requested_by',
            field=models.ForeignKey(related_name='validation_request', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='emailvalidation',
            name='used_by',
            field=models.ForeignKey(related_name='email_validations', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
