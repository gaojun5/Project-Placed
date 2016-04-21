from django.db import models


class ProjectPlatform(models.Model):
    name = models.CharField('Name', max_length=50)

    class Meta:
        verbose_name = "Project Platform"
        verbose_name_plural = "Project Platforms"

    def __str__(self):
        return self.name
