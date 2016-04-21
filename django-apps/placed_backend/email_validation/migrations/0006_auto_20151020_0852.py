# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_validation', '0005_emailvalidation_people_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailvalidation',
            name='type',
            field=models.CharField(max_length=50, verbose_name=b'Type', choices=[(b'invitation', b'Invitation'), (b'confirmation', b'Confirmation'), (b'reset', b'Reset PASSWORD: ')]),
        ),
    ]
