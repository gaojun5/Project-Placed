from django.conf.urls import patterns, url
from project_target_device.views import ProjectTargetDeviceViewSet

project_target_device_list = ProjectTargetDeviceViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

project_target_device_detail = ProjectTargetDeviceViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = patterns(
    '',
    url(r'^$', project_target_device_list, name='project-target-device-list'),
    url(r'^(?P<pk>\d+)$', project_target_device_detail, name='project-target-device-detail'),
)
