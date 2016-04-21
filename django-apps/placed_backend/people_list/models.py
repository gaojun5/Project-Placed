from django.db import models
from django.contrib.auth.models import Group
from course_module.models import CourseModule
import csv


class PeopleList(models.Model):
    name = models.CharField(default="Course List", max_length=50, unique=True)
    group = models.ForeignKey(Group)
    course_wide_list = models.BooleanField('Course Wide List', default=False)
    project_proposal = models.BooleanField('Project proposal', default=False)
    project_assignment = models.BooleanField('Project Assignment', default=False)
    projects_per_year = models.IntegerField('Number of Projects per Year', default=1)
    projects_per_1st_term = models.IntegerField('Number of Projects per 1st term', default=1)
    projects_per_2nd_term = models.IntegerField('Number of Projects per 2nd term', default=1)
    projects_per_3rd_term = models.IntegerField('Number of Projects per 3rd term', default=1)

    project_visibility = models.BooleanField('Project Visibility', default=False)
    send_invitations = models.BooleanField('Send invitations to access a platform', default=False)
    module = models.ForeignKey(CourseModule, null=True)

    class Meta:
        verbose_name = "People List"
        verbose_name_plural = "People Lists"

    def __str__(self):
        return self.name
