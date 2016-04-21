from rest_framework import serializers
from company.models import Company
from project.serializers import ProjectSerializer


class CompanySerializer(serializers.ModelSerializer):
    project_set = ProjectSerializer(many=True)

    class Meta:
        model = Company


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        field = ('name', 'video', 'web_link', 'employees')


class CompanyImageUploadSerializer(serializers.Serializer):
    file = serializers.ImageField()
