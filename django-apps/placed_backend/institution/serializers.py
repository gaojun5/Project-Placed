from rest_framework import serializers
from institution.models import Institution


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
