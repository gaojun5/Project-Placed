from rest_framework import serializers
from email_validation.models import EmailValidation
from placed_user.serializers import PlacedUserSerializer


class EmailValidationSerializer(serializers.ModelSerializer):
    used_by = PlacedUserSerializer()
    requested_by = PlacedUserSerializer()

    class Meta:
        model = EmailValidation
        depth = 2


class EmailValidationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailValidation
        fields = ('type', 'email', 'first_name', 'last_name', 'requested_by', 'group')
