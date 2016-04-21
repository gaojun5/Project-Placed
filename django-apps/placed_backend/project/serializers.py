from rest_framework import serializers
from project.models import Project
from placed_user.serializers import PlacedUserSerializer
from skill.models import Skill
from project_platform.models import ProjectPlatform
from project_data.models import ProjectData
from project_target_device.models import ProjectTargetDevice


class ProjectSerializer(serializers.ModelSerializer):
    students = PlacedUserSerializer(many=True)
    mentors = PlacedUserSerializer(many=True)
    endorser = PlacedUserSerializer(many=True)
    favourite = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    creator = PlacedUserSerializer()

    class Meta:
        model = Project
        fields = ('id', 'title', 'company', 'visibility', 'status', 'mentors', 'endorser', 'students', 'creator', 'desired_start_date', 'desired_end_date', 'term', 'brief', 'scope', 'resources_provided', 'skills_needed', 'skills_practiced', 'module', 'data', 'platform', 'target_device', 'student_needed', 'terms_agreement', 'ip_agreement', 'proposal_date', 'validate', 'assigned', 'favourite', 'image')
        depth = 1


class ProjectCreateSerializer(serializers.ModelSerializer):
    skills_needed = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), many=True, allow_null=True)
    skills_practiced = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), many=True, allow_null=True)
    data = serializers.PrimaryKeyRelatedField(queryset=ProjectData.objects.all(), many=True, allow_null=True)
    platform = serializers.PrimaryKeyRelatedField(queryset=ProjectPlatform.objects.all(), many=True, allow_null=True)
    target_device = serializers.PrimaryKeyRelatedField(queryset=ProjectTargetDevice.objects.all(), many=True, allow_null=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'company', 'desired_start_date', 'desired_end_date', 'brief', 'scope', 'resources_provided', 'skills_needed', 'skills_practiced', 'module', 'data', 'platform', 'target_device', 'terms_agreement', 'ip_agreement', 'proposal_date', 'validate', 'creator')


class ProjectImageUploadSerializer(serializers.Serializer):
    file = serializers.ImageField()
