# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacedUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name=b'Email address')),
                ('first_name', models.CharField(max_length=150, verbose_name=b'First Name')),
                ('last_name', models.CharField(max_length=150, verbose_name=b'Last Name')),
                ('is_staff', models.BooleanField(default=False, verbose_name=b'Staff status')),
                ('is_active', models.BooleanField(default=False, verbose_name=b'Active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Date joined')),
                ('institution', models.CharField(max_length=50, verbose_name=b'Institucion/Company')),
                ('group', models.ForeignKey(to='auth.Group')),
            ],
            options={
                'verbose_name': 'Placed User',
                'verbose_name_plural': 'Placed Users',
            },
        ),
    ]
