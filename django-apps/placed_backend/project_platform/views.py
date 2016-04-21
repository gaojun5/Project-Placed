from rest_framework import viewsets
from project_platform.models import ProjectPlatform
from project_platform.serializers import ProjectPlatformSerializer


class ProjectPlatformViewSet(viewsets.ModelViewSet):
    queryset = ProjectPlatform.objects.all()
    serializer_class = ProjectPlatformSerializer
