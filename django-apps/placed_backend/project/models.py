from django.db import models
from django.core import mail
from django.template import Context
from django.template.loader import get_template
from course_module.models import CourseModule
from skill.models import Skill
from placed_user.models import PlacedUser
from project_data.models import ProjectData
from project_platform.models import ProjectPlatform
from project_target_device.models import ProjectTargetDevice
from company.models import Company
from django.conf import settings
from project.managers import ProjectManager


class Project(models.Model):
    VISIBILITY_CHOICES = (('public', 'Public'), ('private', 'Private'))
    STATUS_CHOICES = (
        ('potential', 'Saved for potential endorsement'),
        ('requested', 'Requested endorsement'),
        ('in_progress', 'Endorsement in Progress'),
        ('endorsed', 'Endorsed'),
        ('assigned', 'Assigned'))
    title = models.CharField("Title", max_length=150)
    company = models.ForeignKey(Company)
    visibility = models.CharField('Visibility', max_length=50, choices=VISIBILITY_CHOICES, default='private')
    status = models.CharField('Status', max_length=50, default='potential', choices=STATUS_CHOICES)
    mentors = models.ManyToManyField(PlacedUser, related_name='projects_mentored')
    endorser = models.ManyToManyField(PlacedUser, related_name='projects_endorsed')
    coordinators = models.ManyToManyField(PlacedUser, related_name='projects_coordinator')
    students = models.ManyToManyField(PlacedUser, related_name='projects_assigned')
    creator = models.ForeignKey(PlacedUser, related_name="projects_created", null=True)
    desired_start_date = models.DateField('Desired Start Date')
    desired_end_date = models.DateField('Desired End Date')
    term = models.IntegerField('Term', default=1)
    brief = models.TextField('Brief')
    scope = models.TextField('Scope', null=True)
    resources_provided = models.TextField('Resources provided', null=True)
    skills_needed = models.ManyToManyField(Skill, related_name='projects_need_it')
    skills_practiced = models.ManyToManyField(Skill, related_name='projects_practise_it')
    module = models.ForeignKey(CourseModule)

    data = models.ManyToManyField(ProjectData)
    platform = models.ManyToManyField(ProjectPlatform)
    target_device = models.ManyToManyField(ProjectTargetDevice)

    #student_needed = models.IntegerField('Students needed')

    terms_agreement = models.URLField('Terms Agreement', null=True)
    ip_agreement = models.URLField('IP Agreement', null=True)
    proposal_date = models.DateTimeField('Proposal Date', auto_now_add=True)
    validate = models.BooleanField('Validate', default=False)
    favourite = models.ManyToManyField(PlacedUser, related_name='favourite_projects')
    image = models.ImageField(upload_to='project/profile', verbose_name='Project Image', null=True)

    objects = ProjectManager()

    @property
    def assigned(self):
        return self.students.count() == self.student_needed

    @property
    def student_needed(self):
        return self.module.students_per_project

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

    def add_student(self, student):
        self.students.add(student)
        # self.send_student_assigned_mail(student)
        # if self.students.count() == self.student_needed:
        #     self.send_assigned_mail()
        return self.save()

    def remove_student(self, student_id):
        student = PlacedUser.objects.get(id=student_id)
        self.students.remove(student)
        return self.save()

    def add_mentor(self, mentor):
        self.mentors.add(mentor)
        # self.send_new_supervisor_mail(mentor)
        return self.save()

    def remove_mentor(self, mentor_id):
        mentor = PlacedUser.objects.get(id=mentor_id)
        self.mentors.remove(mentor)
        return self.save()

    def add_endorser(self, endorser):
        self.endorser.add(endorser)
        self.set_endorsed()
        # self.send_endorsed_mail()
        return self.save()

    def remove_endorser(self, endorser_id):
        endorser = PlacedUser.objects.get(id=endorser_id)
        self.endorser.remove(endorser)
        return self.save()

    def add_favourite(self, favourite_id):
        favourite = PlacedUser.objects.get(id=favourite_id)
        self.favourite.add(favourite)
        return self.save()

    def remove_favourite(self, favourite_id):
        favourite = PlacedUser.objects.get(id=favourite_id)
        self.favourite.remove(favourite)
        return self.save()

    def set_requested(self):
        self.status = 'requested'
        return self.save()

    def set_in_progress(self):
        self.status = 'in_progress'
        return self.save()

    def set_endorsed(self):
        self.status = 'endorsed'
        return self.save()

    def set_assigned(self):
        self.status = 'assigned'
        return self.save()

    def coordinators_mails(self):
        return [coordinator.email for coordinator in self.coordinators.all()]

    def mentors_mails(self):
        return [mentor.email for mentor in self.mentors.all()]

    def students_mails(self):
        return [student.email for student in self.students.all()]

    def send_request_endorsement(self):
        body_template = get_template('mails/request_endorsement.html')
        body_context = Context({'project': self})
        body = body_template.render(body_context)
        mail.send_mail('Placed Request Endorsement', body, self.creator.email, self.coordinators_mails(), fail_silently=False, html_message=body)

    def send_endorsed_mail(self):
        body_template = get_template('mails/project_endorsed.html')
        body_context = Context({'project': self})
        body = body_template.render(body_context)
        mail.send_mail('Placed Request Endorsement', body, settings.ADMIN_EMAIL, [self.creator.email, ], fail_silently=False, html_message=body)

    def send_student_assigned_mail(self, student):
        body_template = get_template('mails/project_assigned_student.html')
        body_context = Context({'project': self})
        body = body_template.render(body_context)
        mail.send_mail('Placed Request Endorsement', body, settings.ADMIN_EMAIL, [student.email, ], fail_silently=False, html_message=body)

    def send_assigned_mail(self):
        body_template = get_template('mails/project_assigned.html')
        body_context = Context({'project': self})
        body = body_template.render(body_context)
        mail.send_mail('Placed Request Endorsement', body, settings.ADMIN_EMAIL, [self.creator.email] + self.mentors_mails(), fail_silently=False, html_message=body)

    def send_new_supervisor_mail(self, supervisor):
        body_template = get_template('mails/project_new_supervisor.html')
        body_context = Context({'project': self, 'supervisor': supervisor})
        body = body_template.render(body_context)
        mail.send_mail('Placed Request Endorsement', body, settings.ADMIN_EMAIL, self.students_mails(), fail_silently=False, html_message=body)
