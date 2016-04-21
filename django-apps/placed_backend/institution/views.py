from rest_framework import viewsets
from institution.models import Institution
from institution.serializers import InstitutionSerializer


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
