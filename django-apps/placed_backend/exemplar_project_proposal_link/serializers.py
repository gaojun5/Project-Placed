from rest_framework import serializers
from exemplar_project_proposal_link.models import ExemplarProjectProposalLink


class ExemplarProjectProposalLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExemplarProjectProposalLink
