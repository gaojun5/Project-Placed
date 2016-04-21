from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated
from project.models import Project
from project.serializers import ProjectSerializer, ProjectCreateSerializer, ProjectImageUploadSerializer
from email_validation.models import EmailValidation
from placed_user.serializers import PlacedUserSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer

    def get_queryset(self):
        # queryset = Project.objects.all()
        list_option = 'track'
        if 'option' in self.request.query_params:
            list_option = self.request.query_params['option']
        queryset = Project.objects.list(self.request.user, list_option)
        if 'title' in self.request.query_params:
            queryset = queryset.filter(title__contains=self.request.query_params['title'])
        if 'skill' in self.request.query_params:
            queryset = queryset.filter(skills_needed__in=self.request.query_params.getlist('skill'))
        if 'term' in self.request.query_params:
            queryset = queryset.filter(term=self.request.query_params['term'])
        if 'status' in self.request.query_params:
            queryset = queryset.filter(status=self.request.query_params['status'])
        if 'order_by' in self.request.query_params:
            queryset = queryset.order_by(self.request.query_params['order_by'])
        return queryset

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProjectCreateSerializer
        return ProjectSerializer

    def get_user_id_from_invitation(self, id):
        invitation = EmailValidation.objects.get(pk=id)
        if not invitation.used_by:
            invitation.generate_user()
        return invitation.used_by

    @detail_route(methods=['post'])
    def add_student(self, request, pk=None):
        project = self.get_object()
        student = self.get_user_id_from_invitation(request.data['id'])
        project.add_student(student)
        return Response({'status': 'OK', 'user': PlacedUserSerializer(student).data})

    @detail_route(methods=['patch'])
    def remove_student(self, request, pk=None):
        project = self.get_object()
        student_id = request.data['id']
        project.remove_student(student_id)
        return Response({'status': 'OK'})

    @detail_route(methods=['post'])
    def add_mentor(self, request, pk=None):
        project = self.get_object()
        mentor = self.get_user_id_from_invitation(request.data['id'])
        project.add_mentor(mentor)
        return Response({'status': 'OK', 'user': PlacedUserSerializer(mentor).data})

    @detail_route(methods=['patch'])
    def remove_mentor(self, request, pk=None):
        project = self.get_object()
        mentor_id = request.data['id']
        project.remove_mentor(mentor_id)
        return Response({'status': 'OK'})

    @detail_route(methods=['post'])
    def add_endorser(self, request, pk=None):
        project = self.get_object()
        endorser = self.get_user_id_from_invitation(request.data['id'])
        project.add_endorser(endorser)
        return Response({'status': 'OK', 'user': PlacedUserSerializer(endorser).data})

    @detail_route(methods=['patch'])
    def remove_endorser(self, request, pk=None):
        project = self.get_object()
        endorser_id = request.data['id']
        project.remove_endorser(endorser_id)
        return Response({'status': 'OK'})

    @detail_route(methods=['post'])
    def add_favourite(self, request, pk=None):
        project = self.get_object()
        favourite_id = request.data['id']
        project.add_favourite(favourite_id)
        return Response({'status': 'OK'})

    @detail_route(methods=['patch'])
    def remove_favourite(self, request, pk=None):
        project = self.get_object()
        favourite_id = request.data['id']
        project.remove_favourite(favourite_id)
        return Response({'status': 'OK'})

    @detail_route(methods=['patch'])
    def confirm_validity(self, request, pk=None):
        project = self.get_object()
        project.set_in_progress()
        return Response({'status': 'OK'})

    @detail_route(methods=['patch'])
    def request_endorsement(self, request, pk=None):
        project = self.get_object()
        # project.send_request_endorsement()
        project.set_requested()
        return Response({'status': 'OK'})


class ProjectImageUploadView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (FileUploadParser,)

    def post(self, request, pk=None):
        image_serializer = ProjectImageUploadSerializer(data=request.data)
        if image_serializer.is_valid():
            project = Project.objects.get(pk=pk)
            project.image = image_serializer.validated_data['file']
            project.save()
            return Response(data=ProjectSerializer(project).data)
        return Response(status=404)
