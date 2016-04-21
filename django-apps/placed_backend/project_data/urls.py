from django.conf.urls import patterns, url
from project_data.views import ProjectDataViewSet

project_data_list = ProjectDataViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

project_data_detail = ProjectDataViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = patterns(
    '',
    url(r'^$', project_data_list, name='project-data-list'),
    url(r'^(?P<pk>\d+)$', project_data_detail, name='project-data-detail'),
)
