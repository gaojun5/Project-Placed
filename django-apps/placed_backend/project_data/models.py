from django.db import models


class ProjectData(models.Model):
    name = models.CharField('Name', max_length=50)

    class Meta:
        verbose_name = "Project Data"
        verbose_name_plural = "Project Datas"

    def __str__(self):
        return self.name
