from rest_framework import serializers
from project_platform.models import ProjectPlatform


class ProjectPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectPlatform
