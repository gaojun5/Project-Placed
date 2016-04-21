# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_auto_20151104_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(default=b'potential', max_length=50, verbose_name=b'Status', choices=[(b'potential', b'Saved for potential endorsement'), (b'requested', b'Requested endorsement'), (b'in_progress', b'Endorsement in Progress'), (b'endorsed', b'Endorsed'), (b'assigned', b'Assigned')]),
        ),
    ]
