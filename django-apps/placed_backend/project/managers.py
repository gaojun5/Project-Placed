from django.db import models


STUDENT_ID = 3
COMPANY_ID = 4
ENDORSER_ID = 5
MENTOR_ID = 6


class ProjectManager(models.Manager):
    def track(self, user):
        if user.group.id == STUDENT_ID:
            return user.projects_assigned.all()
        if user.group.id == ENDORSER_ID:
            return user.projects_endorsed.all()
        if user.group.id == MENTOR_ID:
            return user.projects_mentored.all()
        if user.group.id == COMPANY_ID:
            return self.filter(company__id__in=user.companies.values_list('id', flat=True))
        return self.all()

    def explore(self, user):
        # if user.group.id == STUDENT_ID and not user.project_proposal:
        #     return self.filter(status__in=['endorsed', 'assigned'])
        # if user.group.id == COMPANY_ID:
        #     return self.exclude(status='potential')
        if user.group.id in [STUDENT_ID, COMPANY_ID]:
            return self.none()
        return self.all()

    def list(self, user, list_option):
        if list_option == 'track':
            return self.track(user)
        return self.explore(user)
