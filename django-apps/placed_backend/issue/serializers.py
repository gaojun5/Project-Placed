from rest_framework import serializers
from issue.models import Issue


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
