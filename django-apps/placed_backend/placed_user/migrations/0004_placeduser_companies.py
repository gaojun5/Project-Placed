# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('placed_user', '0003_placeduser_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeduser',
            name='companies',
            field=models.ManyToManyField(related_name='endorsers', to='company.Company'),
        ),
    ]
