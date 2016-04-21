from rest_framework import viewsets
from project_target_device.models import ProjectTargetDevice
from project_target_device.serializers import ProjectTargetDeviceSerializer


class ProjectTargetDeviceViewSet(viewsets.ModelViewSet):
    queryset = ProjectTargetDevice.objects.all()
    serializer_class = ProjectTargetDeviceSerializer
