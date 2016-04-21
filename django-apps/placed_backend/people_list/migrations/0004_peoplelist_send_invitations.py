# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people_list', '0003_auto_20151023_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='peoplelist',
            name='send_invitations',
            field=models.BooleanField(default=False, verbose_name=b'Send invitations to access a platform'),
        ),
    ]
