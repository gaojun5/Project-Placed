from rest_framework import viewsets
from exemplar_project_proposal.models import ExemplarProjectProposal
from exemplar_project_proposal.serializers import ExemplarProjectProposalSerializer


class ExemplarProjectProposalViewSet(viewsets.ModelViewSet):
    queryset = ExemplarProjectProposal.objects.all()
    serializer_class = ExemplarProjectProposalSerializer
