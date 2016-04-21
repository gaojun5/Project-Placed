# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20150922_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='ip_agreement',
            field=models.TextField(null=True, verbose_name=b'IP Agreement'),
        ),
        migrations.AlterField(
            model_name='project',
            name='resources_provided',
            field=models.TextField(null=True, verbose_name=b'Resources provided'),
        ),
        migrations.AlterField(
            model_name='project',
            name='scope',
            field=models.TextField(null=True, verbose_name=b'Scope'),
        ),
        migrations.AlterField(
            model_name='project',
            name='terms_agreement',
            field=models.TextField(null=True, verbose_name=b'Terms Agreement'),
        ),
    ]
