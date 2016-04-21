from django.db import models


class Company(models.Model):
    name = models.CharField('Company Name', max_length=250, unique=True)
    video = models.URLField('Company Video', null=True)
    web_link = models.URLField('Web Link', null=True)
    employees = models.IntegerField('Number of Employees', default=1)
    logo = models.ImageField(upload_to='company/logo', verbose_name='Company Logo', null=True)
    profile_image = models.ImageField(upload_to='company/profile', verbose_name='Profile Image', null=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name
