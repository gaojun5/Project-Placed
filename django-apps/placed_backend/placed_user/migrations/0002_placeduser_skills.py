# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0001_initial'),
        ('placed_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeduser',
            name='skills',
            field=models.ManyToManyField(to='skill.Skill'),
        ),
    ]
