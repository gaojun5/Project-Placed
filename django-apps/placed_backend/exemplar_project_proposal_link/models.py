from django.db import models
from exemplar_project_proposal.models import ExemplarProjectProposal


class ExemplarProjectProposalLink(models.Model):
    link = models.URLField('link')
    description = models.CharField('Description', max_length=50)
    exemplar_project_proporsal = models.ForeignKey(ExemplarProjectProposal, related_name='links')

    class Meta:
        verbose_name = "Exemplar Project Proposal Link"
        verbose_name_plural = "Exemplar Project Proposal Links"
