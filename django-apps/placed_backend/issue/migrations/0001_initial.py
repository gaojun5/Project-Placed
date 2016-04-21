# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=250, verbose_name=b'Subject')),
                ('content', models.TextField(verbose_name=b'Content')),
                ('sender', models.ForeignKey(related_name='issues_sent', to=settings.AUTH_USER_MODEL)),
                ('to', models.ForeignKey(related_name='issues_received', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Issue',
                'verbose_name_plural': 'Issues',
            },
        ),
    ]
