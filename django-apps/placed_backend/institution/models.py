from django.db import models


class Institution(models.Model):
    name = models.CharField("Name", max_length=250)
    min_projects = models.IntegerField("Min projects per supervisor per semester/year")
    max_projects = models.IntegerField("Max projects per supervisor per semester/year")
    students_can_submit_projects = models.BooleanField("Student submitted projects allowed")
    student_visible = models.BooleanField("Student visible")
    max_allocations = models.IntegerField("Max allocations")
    template_project_assignment = models.CharField("Template project assigment", max_length=250)
    template_group_members = models.CharField("Template group members", max_length=250)
    template_invitation = models.CharField("Template invitation", max_length=250)
    template_confirmation = models.CharField("Template confirmation", max_length=250)
    t1_start_date = models.DateField("T1 Start Date")
    t2_start_date = models.DateField("T2 Start Date")
    t3_start_date = models.DateField("T3 Start Date")
    t1_end_date = models.DateField("T1 End Date")
    t2_end_date = models.DateField("T2 End Date")
    t3_end_date = models.DateField("T3 End Date")

    class Meta:
        verbose_name = "Institution"
        verbose_name_plural = "Institutions"

    def __str__(self):
        pass
