import random
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import Group
from django.utils import timezone
from django.core import mail
from django.template import Context
from django.template.loader import get_template
from placed_user.models import PlacedUser
from email_validation.managers import EmailValidationManager
from people_list.models import PeopleList
from django.conf import settings

EXPIRES_DAYS = 30


def default_expires():
    return timezone.now() + timedelta(days=EXPIRES_DAYS)


def default_code():
    return "%032x" % random.getrandbits(128)


class EmailValidation(models.Model):
    INVITATION_TYPE = ('invitation', 'Invitation')
    CONFIRMATION_TYPE = ('confirmation', 'Confirmation')
    RESET_TYPE = ('reset', 'Reset PASSWORD: ')
    TYPES_CHOICES = (INVITATION_TYPE, CONFIRMATION_TYPE, RESET_TYPE)

    type = models.CharField('Type', choices=TYPES_CHOICES, max_length=50, default='confirmation')
    email = models.EmailField('Email')
    first_name = models.CharField('First Name', max_length=250)
    last_name = models.CharField('Last Name', max_length=250)
    code = models.CharField('code', max_length=32, default=default_code)
    expires = models.DateTimeField('Expires', default=default_expires)
    requested_by = models.ForeignKey(PlacedUser, related_name='validation_request')
    used_by = models.ForeignKey(PlacedUser, related_name='email_validations', null=True)
    group = models.ForeignKey(Group)
    people_list = models.ForeignKey(PeopleList, null=True)
    is_used = models.BooleanField(default=False)
    objects = EmailValidationManager()

    class Meta:
        verbose_name = "Email Validation"
        verbose_name_plural = "Email Validations"

    def __str__(self):
        return self.email + " | " + self.code

    @property
    def project_proposal(self):
        return self.people_list.project_proposal

    def generate_user(self):
        self.used_by = PlacedUser.objects.create_user(
            self.email,
            self.first_name,
            self.last_name,
            group=self.group,
            institution=''
        )
        self.save()
        return self.used_by

    def confirm(self):
        if not self.used_by:
            if self.type == 'invitation':
                self.generate_user()
            else:
                self.used_by = self.requested_by
        self.is_used = True
        self.save()
        return self.used_by

    def set_expires(self):
        self.expires = default_expires()

    def has_expired(self):
        return self.expires < timezone.now()

    def is_valid(self):
        return not (self.has_expired() or self.is_used)

    def send_mail(self):
        body_template = get_template('mails/email_validation.html')
        body_context = Context({'invitation': self, 'frontend_url': settings.FRONTEND_URL})
        body = body_template.render(body_context)
        mail.send_mail('Placed Invitation', body, settings.ADMIN_EMAIL, [self.email], fail_silently=False, html_message=body)

    def send_invitation_mail(self):
        body_template = get_template('mails/email_invitation.html')
        body_context = Context({'invitation': self, 'frontend_url': settings.FRONTEND_URL})
        body = body_template.render(body_context)
        mail.send_mail('Placed Invitation', body, settings.ADMIN_EMAIL, [self.email], fail_silently=False, html_message=body)

    def send_reset_password_mail(self):
        body_template = get_template('mails/email_reset_password.html')
        body_context = Context({'invitation': self, 'frontend_url': settings.FRONTEND_URL})
        body = body_template.render(body_context)
        mail.send_mail('Placed Reset Password', body, settings.ADMIN_EMAIL, [self.email], fail_silently=False, html_message=body)
