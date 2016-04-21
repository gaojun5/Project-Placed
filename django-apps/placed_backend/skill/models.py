from django.db import models


class Skill(models.Model):
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name
