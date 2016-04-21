# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_module', '0005_auto_20150922_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemodule',
            name='link',
            field=models.URLField(default='http://ucl.ac.uk', verbose_name=b'Web link'),
            preserve_default=False,
        ),
    ]
