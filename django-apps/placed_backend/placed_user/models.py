from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Group
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from placed_user.managers import PlacedUsedManager
from skill.models import Skill
from course.models import Course
from company.models import Company
from title.models import Title


class PlacedUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email address', max_length=254, unique=True)
    first_name = models.CharField('First Name', max_length=150, null=False)
    last_name = models.CharField("Last Name", max_length=150, null=False)
    is_staff = models.BooleanField('Staff status', default=False)
    is_active = models.BooleanField('Active', default=False)
    date_joined = models.DateTimeField('Date joined', default=timezone.now)

#added 2 additional fields extracted from LinkedIn
    industry = models.CharField('Industry', max_length = 150, null=False)
    location = models.CharField('Location', max_length = 50, null=False)

    institution = models.CharField('Institucion/Company', max_length=50)
    group = models.ForeignKey(Group)
    skills = models.ManyToManyField(Skill)
    course = models.ForeignKey(Course, null=True)
    companies = models.ManyToManyField(Company, related_name='endorsers')
    title = models.ForeignKey(Title, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = PlacedUsedManager()

    class Meta:
        verbose_name = "Placed User"
        verbose_name_plural = "Placed Users"

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def add_skill(self, skill):
        self.skills.add(skill)
        return self.skills.count()

    def set_course(self, course):
        self.course = course
        return self.save()

    def activate(self):
        self.is_active = True
        return self.save()

    def add_company(self, company_id):
        company = Company.objects.get(pk=company_id)
        self.companies.add(company)
        return self.save

    @property
    def assigned(self):
        if self.group.id == 3:
            return self.projects_assigned.count()
        if self.group.id == 4:
            return self.projects_mentored.count()
        return self.projects_endorsed.count()

    @property
    def project_proposal(self):
        if self.group.id == 3:
            email_validation = self.email_validations.filter(type='invitation').first()
            if email_validation:
                return email_validation.project_proposal
            return False
        return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
