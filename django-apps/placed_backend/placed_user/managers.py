from django.contrib.auth.models import BaseUserManager, Group
from title.models import Title


class PlacedUsedManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **other_fields):
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.group = Group.objects.get(name=other_fields['group'])
        if 'title' in other_fields:
            user.title = Title.objects.get(id=other_fields['title'])
        user.institution = other_fields['institution']
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **other_fields):
        user = self.create_user(email, first_name, last_name, password, **other_fields)
        user.is_staff = True
        user.save()
        return user

    def exists(self, email):
        return self.filter(email=email).exists()
