# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExemplarProjectProposal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('video', models.URLField(verbose_name=b'Video link')),
                ('info', models.TextField(verbose_name=b'Exemplar Project Proposal Info')),
            ],
            options={
                'verbose_name': 'Exemplar Project Proposal',
                'verbose_name_plural': 'Exemplar Project Proposals',
            },
        ),
    ]
