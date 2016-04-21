# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20150923_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='company_name',
            field=models.CharField(default='UCL', max_length=50, verbose_name=b'Company Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='ip_agreement',
            field=models.URLField(null=True, verbose_name=b'IP Agreement'),
        ),
        migrations.AlterField(
            model_name='project',
            name='terms_agreement',
            field=models.URLField(null=True, verbose_name=b'Terms Agreement'),
        ),
    ]
