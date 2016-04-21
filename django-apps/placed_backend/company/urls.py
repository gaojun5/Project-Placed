from django.conf.urls import patterns, url
from company.views import CompanyViewSet, CompanyProfileUploadView, CompanyLogoUploadView
company_list = CompanyViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

company_detail = CompanyViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = patterns(
    '',
    url(r'^$', company_list, name='company-list'),
    url(r'^(?P<pk>\d+)$', company_detail, name='company-detail'),
    url(r'^(?P<pk>\d+)/upload/logo$', CompanyLogoUploadView.as_view(), name='company-upload-logo'),
    url(r'^(?P<pk>\d+)/upload/profile$', CompanyProfileUploadView.as_view(), name='company-upload-profile'),
)
