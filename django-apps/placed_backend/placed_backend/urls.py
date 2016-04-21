"""placed_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/1/users/', include('placed_user.urls')),
    url(r'^api/1/skills/', include('skill.urls')),
    url(r'^api/1/courses/', include('course.urls')),
    url(r'^api/1/modules/', include('course_module.urls')),
    url(r'^api/1/projects/', include('project.urls')),
    url(r'^api/1/email/validation/', include('email_validation.urls')),
    url(r'^api/1/exemplar/project/proposals/', include('exemplar_project_proposal.urls')),
    url(r'^api/1/exemplar/project/proposals/link/', include('exemplar_project_proposal_link.urls')),
    url(r'^api/1/people/list/', include('people_list.urls')),
    url(r'^api/1/project/data/', include('project_data.urls')),
    url(r'^api/1/project/platform/', include('project_platform.urls')),
    url(r'^api/1/project/platform/', include('project_platform.urls')),
    url(r'^api/1/project/target/device/', include('project_target_device.urls')),
    url(r'^api/1/institution/', include('institution.urls')),
    url(r'^api/1/company/', include('company.urls')),
    url(r'^api/1/issue/', include('issue.urls')),
    url(r'^api/1/title/', include('title.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
