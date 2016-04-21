# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name=b'Name')),
                ('min_projects', models.IntegerField(verbose_name=b'Min projects per supervisor per semester/year')),
                ('max_projects', models.IntegerField(verbose_name=b'Max projects per supervisor per semester/year')),
                ('students_can_submit_projects', models.BooleanField(verbose_name=b'Student submitted projects allowed')),
                ('student_visible', models.BooleanField(verbose_name=b'Student visible')),
                ('max_allocations', models.IntegerField(verbose_name=b'Max allocations')),
                ('template_project_assignment', models.CharField(max_length=250, verbose_name=b'Template project assigment')),
                ('template_group_members', models.CharField(max_length=250, verbose_name=b'Template group members')),
                ('template_invitation', models.CharField(max_length=250, verbose_name=b'Template invitation')),
                ('template_confirmation', models.CharField(max_length=250, verbose_name=b'Template confirmation')),
                ('t1_start_date', models.DateField(verbose_name=b'T1 Start Date')),
                ('t2_start_date', models.DateField(verbose_name=b'T2 Start Date')),
                ('t3_start_date', models.DateField(verbose_name=b'T3 Start Date')),
                ('t1_end_date', models.DateField(verbose_name=b'T1 End Date')),
                ('t2_end_date', models.DateField(verbose_name=b'T2 End Date')),
                ('t3_end_date', models.DateField(verbose_name=b'T3 End Date')),
            ],
            options={
                'verbose_name': 'Institution',
                'verbose_name_plural': 'Institutions',
            },
        ),
    ]
