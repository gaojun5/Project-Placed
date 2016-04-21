from django.conf.urls import patterns, url
from course.views import CourseViewSet

course_list = CourseViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

course_detail = CourseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = patterns(
    '',
    url(r'^$', course_list, name='course-list'),
    url(r'^(?P<pk>\d+)$', course_detail, name='course-detail'),
)
