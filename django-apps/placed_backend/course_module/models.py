from django.db import models
from skill.models import Skill
from placed_user.models import PlacedUser
from exemplar_project_proposal.models import ExemplarProjectProposal
from course.models import Course


class CourseModule(models.Model):
    name = models.CharField(default="Module name", max_length=50)
    academic_name = models.CharField('Academic name', max_length=250, default="")
    display_name = models.CharField('Display name', max_length=250, default="")
    project_coordinator = models.ForeignKey(PlacedUser)
    project_scope = models.TextField('Project Scope')
    students_per_project = models.IntegerField("Number students per Project")
    Timeline = models.TextField('Timeline', null=True)
    skills = models.ManyToManyField(Skill)
    resources = models.CharField('Resources', max_length=50, null=True)
    other = models.TextField("Other", null=True)
    agreements = models.TextField("Agreements", null=True)
    exemplar_project_proposal = models.ForeignKey(ExemplarProjectProposal, null=True)
    course = models.ForeignKey(Course)
    link = models.URLField("Web link")

    class Meta:
        verbose_name = "Course Module"
        verbose_name_plural = "Course Modules"

    def __str__(self):
        return self.name
