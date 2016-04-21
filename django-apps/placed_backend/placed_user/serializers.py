from django.contrib.auth.models import Group
from placed_user.models import PlacedUser
from project.models import Project
from rest_framework import serializers


class groupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class ProjectSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title')


class PlacedUserSerializer(serializers.ModelSerializer):
    group = groupSerializer()
    projects_assigned = ProjectSimpleSerializer(many=True)
    projects_endorsed = ProjectSimpleSerializer(many=True)
    projects_mentored = ProjectSimpleSerializer(many=True)

    class Meta:
        model = PlacedUser
        fields = ('id', 'email', 'first_name', 'last_name', 'group', 'skills', 'institution', 'course', 'projects_assigned', 'projects_endorsed', 'projects_mentored', 'projects_coordinator', 'assigned', 'project_proposal', 'companies')
        depth = 1
