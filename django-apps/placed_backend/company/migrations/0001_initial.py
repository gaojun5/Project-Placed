# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=250, verbose_name=b'Company Name')),
                ('video', models.URLField(null=True, verbose_name=b'Company Video')),
                ('web_link', models.URLField(null=True, verbose_name=b'Web Link')),
                ('employees', models.IntegerField(default=1, verbose_name=b'Number of Employees')),
                ('logo', models.ImageField(upload_to=b'company/logo', null=True, verbose_name=b'Company Logo')),
                ('profile_image', models.ImageField(upload_to=b'company/profile', null=True, verbose_name=b'Profile Image')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
    ]
