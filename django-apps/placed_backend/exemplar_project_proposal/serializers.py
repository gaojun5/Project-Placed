from rest_framework import serializers
from exemplar_project_proposal.models import ExemplarProjectProposal


class ExemplarProjectProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExemplarProjectProposal
        depth = 1
        fields = ('id', 'video', 'info', 'links')
