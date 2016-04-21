from rest_framework.views import APIView
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from placed_user.models import PlacedUser
from placed_user.serializers import PlacedUserSerializer
from skill.models import Skill
from course.models import Course
from email_validation.models import EmailValidation


class MyUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = PlacedUserSerializer(request.user).data
        return Response(content)


class RegisterView(APIView):
    def post(self, request, format=None):
        try:
            user = PlacedUser.objects.create_user(
                request.data['email'],
                request.data['first_name'],
                request.data['last_name'],
                group=request.data['group'],
                institution=request.data['institution'],
                title=request.data.get('title'))

            email_validation = EmailValidation.objects.create(
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
                requested_by=user,
                group=user.group,
                type='confirmation'
                )
            email_validation.send_mail()
            return Response({'id': user.id}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({'error': "Email already registered"}, status=status.HTTP_400_BAD_REQUEST)

def printname_self(request):
    # get user, return the currently active User model
    User = get_user_model()
    # current user,
    user = User.objects.get(username=request.user)
    # in-built helper method
    social = user.social_auth.get(provider='linkedin-oauth2')
    asd = social.extra_data['access_token']
    # make request
    header = {'Authorization' : 'Bearer' + asd }
    r = requests.get("https://api.linkedin.com/v1/people/~:(first-name,last-name,email-address,location:(name),industry)?format=json", headers=header )
    target = open('/Users/jessietan/Desktop/linkedindata.json', 'w') //need to change
    target.write( json.dumps(r.json()).strip())
    target.close()
    subprocess.call("php /Users/jessietan/Desktop/var-backend2/django-apps/placed_backend/conversion/linkedindata_json2mysql.php", shell=True) // need to change
    return JsonResponse(r.json())



class SetPasswordView(APIView):
    def patch(self, request, user_id, format=None):
        user = PlacedUser.objects.get(id=user_id)
        print user
        user.set_password(request.data['password'])
        user.activate()
        user.save()
        print user
        return Response({'id': user.id})


class ResetPasswordView(APIView):
    def patch(self, request, format=None):
        user_find = PlacedUser.objects.filter(email=request.data['email'])
        if (not user_find.exists()):
            return Response({'result': 'ERROR', 'message': 'Are you sure this is the email you are registered to Project Placed?'})
        user = user_find.first()
        reset_pasword_mail = EmailValidation.objects.create_reset_password_request(user)
        reset_pasword_mail.send_reset_password_mail()
        return Response({'result': 'OK'})


class SelectSkillsView(APIView):
    def patch(self, request, user_id, format=None):
        user = PlacedUser.objects.get(id=user_id)
        for skill in request.data:
            user_skill = Skill.objects.get(id=skill['id'])
            user.add_skill(user_skill)
        return Response({'id': user.id})


class SelectCourseView(APIView):
    def patch(self, request, user_id, format=None):
        user = PlacedUser.objects.get(id=user_id)
        course = Course.objects.get(id=request.data['id'])
        user.set_course(course)
        return Response({'id': user.id})


class GetUserView(generics.RetrieveAPIView):
    queryset = PlacedUser.objects.all()
    serializer_class = PlacedUserSerializer


class GetCoordinatorsView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = PlacedUser.objects.filter(group__id=1)
    serializer_class = PlacedUserSerializer

@login_required(login_url='/skill_mysql2csv/')
def skill_mysql2csv(request):
    subprocess.call("php placed_user/skill_mysql2csv.php", shell=True)
    return redirect('/')

@login_required(login_url='/skill_mysql2json/')
def skill_mysql2json(request):
    subprocess.call("php placed_user/skill_mysql2json.php", shell=True)
    return redirect('/')

@login_required(login_url='/project_mysql2csv/')
def project_mysql2csv(request):
    subprocess.call("php placed_user/project_mysql2csv.php", shell=True)
    return redirect('/')

@login_required(login_url='/project_mysql2json/')
def project_mysql2json(request):
    subprocess.call("php placed_user/project_mysql2json.php", shell=True)
    return redirect('/')

@login_required(login_url='/uploadusercsv/')
def uploadusercsv(request):
    subprocess.call("php placed_user/user_csv2mysql.php", shell=True)
    return render_to_response('home.html')
