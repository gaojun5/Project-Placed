from django.conf.urls import patterns, url
from course_module.views import CourseModuleViewSet

course_module_list = CourseModuleViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

course_module_detail = CourseModuleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = patterns(
    '',
    url(r'^$', course_module_list, name='course-module-list'),
    url(r'^(?P<pk>\d+)$', course_module_detail, name='course-module-detail'),
)
