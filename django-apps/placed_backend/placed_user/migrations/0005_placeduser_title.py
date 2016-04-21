# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('title', '0001_initial'),
        ('placed_user', '0004_placeduser_companies'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeduser',
            name='title',
            field=models.ForeignKey(to='title.Title', null=True),
        ),
    ]
