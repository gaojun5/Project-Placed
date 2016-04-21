from django.db import models


class ExemplarProjectProposal(models.Model):
    video = models.URLField('Video link')
    info = models.TextField('Exemplar Project Proposal Info')

    class Meta:
        verbose_name = "Exemplar Project Proposal"
        verbose_name_plural = "Exemplar Project Proposals"
