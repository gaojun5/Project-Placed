# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people_list', '0002_peoplelist_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='peoplelist',
            name='projects_per_1st_term',
            field=models.IntegerField(default=1, verbose_name=b'Number of Projects per 1st term'),
        ),
        migrations.AddField(
            model_name='peoplelist',
            name='projects_per_2nd_term',
            field=models.IntegerField(default=1, verbose_name=b'Number of Projects per 2nd term'),
        ),
        migrations.AddField(
            model_name='peoplelist',
            name='projects_per_3rd_term',
            field=models.IntegerField(default=1, verbose_name=b'Number of Projects per 3rd term'),
        ),
        migrations.AlterField(
            model_name='peoplelist',
            name='name',
            field=models.CharField(default=b'Course List', unique=True, max_length=50),
        ),
    ]
