from rest_framework import serializers
from project_data.models import ProjectData


class ProjectDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectData
