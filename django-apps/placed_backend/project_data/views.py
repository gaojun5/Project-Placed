from rest_framework import viewsets
from project_data.models import ProjectData
from project_data.serializers import ProjectDataSerializer


class ProjectDataViewSet(viewsets.ModelViewSet):
    queryset = ProjectData.objects.all()
    serializer_class = ProjectDataSerializer
