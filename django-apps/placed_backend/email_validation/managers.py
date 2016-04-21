import csv
from django.db import models


class EmailValidationManager(models.Manager):
    def exists(self, email, code):
        return self.filter(email=email, code=code).exists()

    def exists_in_list(self, email):
        return self.filter(email=email, type='invitation', people_list__isnull=True).exists()

    def get_info(self, email, code, validation_type):
        return self.get(email=email, code=code, type=validation_type, used_by__isnull=True)

    def is_valid(self, email, code):
        if self.exists(email, code):
            return self.get_info(email, code).is_valid()
        return False

    def create_reset_password_request(self, user):
        return self.create(
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            requested_by=user,
            group=user.group,
            type='reset'
        )

    def create_invitation(self, people_list, member, requested_by):
        return self.create(
            type='invitation',
            email=member['email'],
            first_name=member['first_name'],
            last_name=member['last_name'],
            requested_by=requested_by,
            group=people_list.group,
            people_list=people_list
        )

    def add_members(self, people_list, request):
        file = request.data['file']
        csv_reader = csv.DictReader(file)
        import_result = {
            'added': 0,
            'members': []
        }
        for member in csv_reader:
            if not self.exists_in_list(member['email']):
                member = self.create_invitation(people_list, member, request.user)
                import_result['members'].append(member)
        import_result['added'] = len(import_result['members'])
        return import_result
