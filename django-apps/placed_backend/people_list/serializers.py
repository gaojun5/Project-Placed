from rest_framework import serializers
from people_list.models import PeopleList
from email_validation.serializers import EmailValidationSerializer


class PeopleListSerializer(serializers.ModelSerializer):
    emailvalidation_set = EmailValidationSerializer(many=True)

    class Meta:
        model = PeopleList
        depth = 3
        fields = ('id', 'name', 'group', 'course_wide_list', 'project_proposal', 'project_assignment', 'projects_per_year', 'project_visibility', 'module', 'emailvalidation_set')


class PeopleListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeopleList
