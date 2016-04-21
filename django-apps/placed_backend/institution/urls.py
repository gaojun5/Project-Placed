from django.conf.urls import patterns, url
from institution.views import InstitutionViewSet

institution_list = InstitutionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

institution_detail = InstitutionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = patterns(
    '',
    url(r'^$', institution_list, name='institution-list'),
    url(r'^(?P<pk>\d+)$', institution_detail, name='institution-detail'),
)
