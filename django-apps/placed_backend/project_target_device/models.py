from django.db import models


class ProjectTargetDevice(models.Model):
    name = models.CharField('Name', max_length=50)

    class Meta:
        verbose_name = "Project Target Device"
        verbose_name_plural = "Project Target Devices"

    def __str__(self):
        return self.name
