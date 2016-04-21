from django.conf.urls import patterns, url
from rest_framework.authtoken import views
from placed_user.views import RegisterView, SetPasswordView, SelectSkillsView
from placed_user.views import SelectCourseView, MyUserView, GetUserView, ResetPasswordView, GetCoordinatorsView
from placed_user import views

urlpatterns = patterns(
    '',
    url(r'^me$', MyUserView.as_view(),),
    url(r'^register$', RegisterView.as_view(),),
    url(r'^(?P<user_id>\d+)/set-password$', SetPasswordView.as_view(),),
    url(r'^reset/password$', ResetPasswordView.as_view(),),
    url(r'^(?P<user_id>\d+)/skills$', SelectSkillsView.as_view(),),
    url(r'^(?P<user_id>\d+)/course$', SelectCourseView.as_view(),),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^(?P<pk>\d+)$', GetUserView.as_view(),),
    url(r'^coordinator$', GetCoordinatorsView.as_view(),),
    url(r'^skill_mysql2csv/$', 'placed_user.views.skill_mysql2csv'),
    url(r'^skill_mysql2json/$', 'placed_user.views.skill_mysql2json')
    url(r'^project_mysql2csv/$', 'placed_user.views.project_mysql2csv'),
    url(r'^project_mysql2json/$', 'placed_user.views.project_mysql2json'),
    url(r'^user_csv2mysql/$', 'placed_user.views.user_csv2mysql'),
   
)
