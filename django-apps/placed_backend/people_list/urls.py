from django.conf.urls import patterns, url
from people_list.views import PeopleListViewSet, ImportMemberListFileView

people_list_list = PeopleListViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

people_list_detail = PeopleListViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = patterns(
    '',
    url(r'^$', people_list_list, name='people-list-list'),
    url(r'^(?P<pk>\d+)$', people_list_detail, name='people-list-detail'),
    url(r'^(?P<pk>\d+)/import$', ImportMemberListFileView.as_view(), name='people-list-import'),
)
