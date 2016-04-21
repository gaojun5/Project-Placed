from django.conf.urls import patterns, url
from skill.views import SkillView

urlpatterns = patterns(
    '',
    url(r'^skills/$', SkillView.as_view(),),
)
