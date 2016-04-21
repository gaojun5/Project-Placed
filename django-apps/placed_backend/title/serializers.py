from rest_framework import serializers
from title.models import Title


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
