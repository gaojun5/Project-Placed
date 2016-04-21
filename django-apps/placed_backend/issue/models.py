from django.db import models
from django.core import mail
from placed_user.models import PlacedUser


class Issue(models.Model):
    sender = models.ForeignKey(PlacedUser, related_name='issues_sent')
    to = models.ForeignKey(PlacedUser, related_name='issues_received', null=True)
    subject = models.CharField("Subject", max_length=250)
    content = models.TextField("Content")

    class Meta:
        verbose_name = "Issue"
        verbose_name_plural = "Issues"

    def __str__(self):
        return self.subject

    def send_mail(self):
        if self.to is None:
            self.to = PlacedUser.object.get(id=1)
            self.save
        mail.send_mail(self.subject, self.content, self.sender.email, [self.to.email], fail_silently=False, html_message=self.content)

    def save(self, *args, **kwargs):
        super(Issue, self).save(*args, **kwargs)
        self.send_mail()
