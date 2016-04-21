from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from people_list.models import PeopleList
from people_list.serializers import PeopleListSerializer, PeopleListCreateSerializer
from email_validation.models import EmailValidation
from email_validation.serializers import EmailValidationSerializer


class PeopleListViewSet(viewsets.ModelViewSet):
    queryset = PeopleList.objects.all()
    serializer_class = PeopleListSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PeopleListCreateSerializer
        return PeopleListSerializer


class ImportMemberListFileView(APIView):
    parser_classes = (FileUploadParser,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk=None):
        people_list = PeopleList.objects.get(pk=pk)
        import_result = EmailValidation.objects.add_members(people_list, request)
        if import_result['added'] == 0:
            return Response(data=import_result, status=204)
        import_result['members'] = EmailValidationSerializer(import_result['members'], many=True).data
        return Response(data=import_result, status=201)
