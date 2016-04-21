from rest_framework import serializers
from project_target_device.models import ProjectTargetDevice


class ProjectTargetDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTargetDevice
