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
            name='EmailValidation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=50, verbose_name=b'Type', choices=[(b'invitation', b'Invitation'), (b'confirmation', b'Confirmation')])),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
                ('first_name', models.CharField(max_length=250, verbose_name=b'First Name')),
                ('last_name', models.CharField(max_length=250, verbose_name=b'Last Name')),
                ('code', models.CharField(max_length=50, verbose_name=b'code')),
                ('expires', models.DateTimeField(verbose_name=b'Expires')),
                ('requested_by', models.ForeignKey(related_name='requested_by_user', to=settings.AUTH_USER_MODEL)),
                ('used_by', models.ForeignKey(related_name='used_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Email Validation',
                'verbose_name_plural': 'Email Validations',
            },
        ),
    ]
