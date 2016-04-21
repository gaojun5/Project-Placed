from django.conf.urls import patterns, url
from title.views import TitleListView

urlpatterns = patterns(
    '',
    url(r'^(?P<group_id>\d+)$', TitleListView.as_view(),),
)
