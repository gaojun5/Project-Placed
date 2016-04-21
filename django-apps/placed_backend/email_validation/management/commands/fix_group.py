from django.core.management.base import BaseCommand
from email_validation.models import EmailValidation


class Command(BaseCommand):
    def handle(self, *args, **options):
        for email_validation in EmailValidation.objects.all():
            if email_validation.used_by:
                print email_validation.used_by.group, email_validation.group
                email_validation.used_by.group = email_validation.group
                email_validation.used_by.save()
