# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_module', '0002_coursemodule_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodule',
            name='exemplar_project_proposal',
            field=models.ForeignKey(to='exemplar_project_proposal.ExemplarProjectProposal', null=True),
        ),
    ]
