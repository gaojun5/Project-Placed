# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'Title')),
                ('group', models.ForeignKey(to='auth.Group')),
            ],
            options={
                'verbose_name': 'Title',
                'verbose_name_plural': 'Titles',
            },
        ),
    ]
