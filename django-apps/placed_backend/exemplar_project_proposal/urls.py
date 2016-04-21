from django.conf.urls import patterns, url
from exemplar_project_proposal.views import ExemplarProjectProposalViewSet

exemplar_project_proposal_list = ExemplarProjectProposalViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

exemplar_project_proposal_detail = ExemplarProjectProposalViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = patterns(
    '',
    url(r'^$', exemplar_project_proposal_list, name='exemplar-project-proposal-list'),
    url(r'^(?P<pk>\d+)$', exemplar_project_proposal_detail, name='exemplar-project-proposal-detail'),
)
