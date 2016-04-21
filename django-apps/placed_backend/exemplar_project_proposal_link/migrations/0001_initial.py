# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exemplar_project_proposal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExemplarProjectProposalLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.URLField(verbose_name=b'link')),
                ('description', models.CharField(max_length=50, verbose_name=b'Description')),
                ('exemplar_project_proporsal', models.ForeignKey(related_name='links', to='exemplar_project_proposal.ExemplarProjectProposal')),
            ],
            options={
                'verbose_name': 'Exemplar Project Proposal Link',
                'verbose_name_plural': 'Exemplar Project Proposal Links',
            },
        ),
    ]
