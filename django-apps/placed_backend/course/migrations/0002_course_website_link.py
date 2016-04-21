# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='website_link',
            field=models.URLField(null=True, verbose_name=b'Website Link'),
        ),
    ]
