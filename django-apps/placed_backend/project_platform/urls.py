from django.conf.urls import patterns, url
from project_platform.views import ProjectPlatformViewSet

project_platform_list = ProjectPlatformViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

project_platform_detail = ProjectPlatformViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = patterns(
    '',
    url(r'^$', project_platform_list, name='project-platform-list'),
    url(r'^(?P<pk>\d+)$', project_platform_detail, name='project-platform-detail'),
)
