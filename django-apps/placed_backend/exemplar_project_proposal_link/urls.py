from django.conf.urls import patterns, url
from exemplar_project_proposal_link.views import ExemplarProjectProposalLinkViewSet

exemplar_project_proposal_link_list = ExemplarProjectProposalLinkViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

exemplar_project_proposal_link_detail = ExemplarProjectProposalLinkViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = patterns(
    '',
    url(r'^$', exemplar_project_proposal_link_list, name='exemplar-project-proposal-link-list'),
    url(r'^(?P<pk>\d+)$', exemplar_project_proposal_link_detail, name='exemplar-project-proposal-link-detail'),
)
