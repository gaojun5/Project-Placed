# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20150923_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='proposal_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 5, 10, 18, 4, 882068, tzinfo=utc), verbose_name=b'Proposal Date', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='term',
            field=models.IntegerField(default=1, verbose_name=b'Term'),
        ),
    ]
