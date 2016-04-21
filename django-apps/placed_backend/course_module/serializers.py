from rest_framework import serializers
from course_module.models import CourseModule
from exemplar_project_proposal.serializers import ExemplarProjectProposalSerializer
from project.serializers import ProjectSerializer


class CourseModuleSerializer(serializers.ModelSerializer):
    exemplar_project_proposal = ExemplarProjectProposalSerializer()
    project_set = ProjectSerializer(many=True)

    class Meta:
        model = CourseModule
        depth = 1


class CourseModuleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModule
