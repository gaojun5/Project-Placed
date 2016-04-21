from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from company.models import Company
from company.serializers import CompanyCreateSerializer, CompanySerializer, CompanyImageUploadSerializer

import subprocess
import json
from sys import argv

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CompanyCreateSerializer
        return CompanySerializer

    @login_required(login_url='/mysql2json/')
    def company_mysql2json(request):
         subprocess.call("php company/company_mysql2json.php", shell=True)
         return redirect ('/')
    
    @login_required(login_url='/mysql2csv/')
    def company_mysql2csv(request):
         subprocess.call("php company/company_mysql2csv.php", shell=True)
         return redirect('/')

class CompanyLogoUploadView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (FileUploadParser,)

    def post(self, request, pk=None):
        image_serializer = CompanyImageUploadSerializer(data=request.data)
        if image_serializer.is_valid():
            company = Company.objects.get(pk=pk)
            company.logo = image_serializer.validated_data['file']
            company.save()
            return Response(data=CompanySerializer(company).data)
        return Response(status=404)


class CompanyProfileUploadView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (FileUploadParser,)

    def post(self, request, pk=None):
        image_serializer = CompanyImageUploadSerializer(data=request.data)
        if image_serializer.is_valid():
            company = Company.objects.get(pk=pk)
            company.profile_image = image_serializer.validated_data['file']
            company.save()
            return Response(data=CompanySerializer(company).data)
        return Response(status=404)
