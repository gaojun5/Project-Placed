from django.db import models


class Course(models.Model):
    name = models.CharField(default="Course without name", max_length=50)
    website_link = models.URLField("Website Link", null=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.name
