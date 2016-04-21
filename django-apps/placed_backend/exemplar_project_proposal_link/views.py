from rest_framework import viewsets
from exemplar_project_proposal_link.models import ExemplarProjectProposalLink
from exemplar_project_proposal_link.serializers import ExemplarProjectProposalLinkSerializer


class ExemplarProjectProposalLinkViewSet(viewsets.ModelViewSet):
    queryset = ExemplarProjectProposalLink.objects.all()
    serializer_class = ExemplarProjectProposalLinkSerializer
