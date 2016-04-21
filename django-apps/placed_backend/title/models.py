from django.db import models
from django.contrib.auth.models import Group


class Title(models.Model):
    title = models.CharField("Title", max_length=50)
    group = models.ForeignKey(Group)

    class Meta:
        verbose_name = "Title"
        verbose_name_plural = "Titles"

    def __str__(self):
        return self.title
