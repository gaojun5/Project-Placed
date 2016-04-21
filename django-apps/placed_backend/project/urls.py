from django.conf.urls import patterns, url
from project.views import ProjectViewSet, ProjectImageUploadView

project_list = ProjectViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

project_detail = ProjectViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

project_students_add = ProjectViewSet.as_view({
    'post': 'add_student'
})

project_students_remove = ProjectViewSet.as_view({
    'patch': 'remove_student'
})

project_mentor_add = ProjectViewSet.as_view({
    'post': 'add_mentor'
})

project_mentor_remove = ProjectViewSet.as_view({
    'patch': 'remove_mentor'
})

project_endorsers_add = ProjectViewSet.as_view({
    'post': 'add_endorser'
})

project_endorsers_remove = ProjectViewSet.as_view({
    'patch': 'remove_endorser'
})

project_favourites_add = ProjectViewSet.as_view({
    'post': 'add_favourite'
})

project_favourites_remove = ProjectViewSet.as_view({
    'patch': 'remove_favourite'
})

project_confirm_validity = ProjectViewSet.as_view({
    'patch': 'confirm_validity'
})

project_request_endorsement = ProjectViewSet.as_view({
    'patch': 'request_endorsement'
})

urlpatterns = patterns(
    '',
    url(r'^$', project_list, name='project-list'),
    url(r'^(?P<pk>\d+)$', project_detail, name='project-detail'),
    url(r'^(?P<pk>\d+)/student/add$', project_students_add, name='project-students-add'),
    url(r'^(?P<pk>\d+)/student/remove$', project_students_remove, name='project-students-remove'),
    url(r'^(?P<pk>\d+)/mentor/add$', project_mentor_add, name='project-mentor-add'),
    url(r'^(?P<pk>\d+)/mentor/remove$', project_mentor_remove, name='project-mentor-remove'),
    url(r'^(?P<pk>\d+)/endorser/add$', project_endorsers_add, name='project-endorsers-add'),
    url(r'^(?P<pk>\d+)/endorser/remove$', project_endorsers_remove, name='project-endorsers-remove'),
    url(r'^(?P<pk>\d+)/favourite/add$', project_favourites_add, name='project-favourites-add'),
    url(r'^(?P<pk>\d+)/favourite/remove$', project_favourites_remove, name='project-favourites-remove'),
    url(r'^(?P<pk>\d+)/confirm/validity$', project_confirm_validity, name='project-confirm-validity'),
    url(r'^(?P<pk>\d+)/request/endorsement$', project_confirm_validity, name='project-request-endorsement'),
    url(r'^(?P<pk>\d+)/upload/image$', ProjectImageUploadView.as_view(), name='project-upload-image'),
)
