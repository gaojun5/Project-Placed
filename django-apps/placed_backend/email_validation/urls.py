from django.conf.urls import patterns, url
from email_validation.views import ValidationCheckView, RequestInvitationView, ResendInvitationView, ListInvitationView, RetrieveInvitationView, SendInvitationView


urlpatterns = patterns(
    '',
    url(r'^check$', ValidationCheckView.as_view(),),
    url(r'^request/invitation/$', RequestInvitationView.as_view(),),
    url(r'^resend/invitation/$', ResendInvitationView.as_view(),),
    url(r'^list/(?P<list_id>\d+)$', ListInvitationView.as_view(),),
    url(r'^(?P<pk>\d+)$', RetrieveInvitationView.as_view(),),
    url(r'^send/invitation/$', SendInvitationView.as_view(),),
)
