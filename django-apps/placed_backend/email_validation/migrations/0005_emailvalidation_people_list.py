# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people_list', '0002_peoplelist_module'),
        ('email_validation', '0004_auto_20150907_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailvalidation',
            name='people_list',
            field=models.ForeignKey(to='people_list.PeopleList', null=True),
        ),
    ]
