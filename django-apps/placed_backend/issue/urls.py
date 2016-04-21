from django.conf.urls import patterns, url
from issue.views import IssueViewSet

issue_list = IssueViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

issue_detail = IssueViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = patterns(
    '',
    url(r'^$', issue_list, name='issue-list'),
    url(r'^(?P<pk>\d+)$', issue_detail, name='issue-detail'),
)
