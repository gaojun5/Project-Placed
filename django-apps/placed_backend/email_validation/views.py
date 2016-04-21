from django.core import mail
from django.template import Context
from django.template.loader import get_template
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from email_validation.models import EmailValidation
from placed_user.models import PlacedUser
from email_validation.serializers import EmailValidationSerializer, EmailValidationCreateSerializer


class ValidationCheckView(APIView):
    def get(self, request, format=None):
        content = {'valid': False, 'expired': False}
        params = self.request.query_params
        validation_type = 'confirmation'
        if 'type' in params:
            validation_type = params['type']
        if 'code' in params and 'email' in params:
            email_validation = EmailValidation.objects.get_info(params['email'], params['code'], validation_type)
            if email_validation.is_valid():
                content['valid'] = True
                email_validation.confirm()
                content['user'] = EmailValidationSerializer(email_validation).data
            else:
                content['expired'] = email_validation.has_expired()
        print content
        return Response(content)


class RequestInvitationView(APIView):
    def get(self, request, format=None):
        content = {
            'duplicated': False,
            'sent': False
        }
        params = self.request.query_params
        if EmailValidation.objects.filter(email=params['email'], group__name=params['group']).exists():
            content['duplicated'] = True
        else:
            body_template = get_template('mails/request_invitation.html')
            body_context = Context({'mail': params['email'], 'group': params['group']})
            body = body_template.render(body_context)
            mail.send_mail('Request Invitation', body, 'admin@placed.ucl.ac.uk', ['admin@placed.ucl.ac.uk'], fail_silently=False)
            content['sent'] = True
        return Response(content)


class ResendInvitationView(APIView):
    def get(self, request, format=None):
        params = self.request.query_params
        email_validation = EmailValidation.objects.get(email=params['email'])
        email_validation.send_mail()
        content = {
            'sent': True
        }
        return Response(content)


class ListInvitationView(APIView):
    def get(self, request, list_id, format=None):
        queryset = EmailValidation.objects.filter(people_list=list_id)
        if 'skill' in request.query_params:
            queryset = queryset.filter(used_by__skills__name=request.query_params['skill'])
        if 'order_by' in request.query_params:
            queryset = queryset.order_by(request.query_params['order_by'])
        serializer = EmailValidationSerializer(queryset, many=True)
        return Response(serializer.data)


class RetrieveInvitationView(generics.RetrieveAPIView):
    queryset = EmailValidation.objects.all()
    serializer_class = EmailValidationSerializer


class SendInvitationView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        request.data['requested_by'] = request.user.id
        request.data['used_by'] = None
        invitation_serializer = EmailValidationCreateSerializer(data=request.data)

        if not PlacedUser.objects.exists(request.data['email']) and invitation_serializer.is_valid():
            invitation = invitation_serializer.save()
            invitation.send_invitation_mail()
            return Response(invitation_serializer.data, status=status.HTTP_201_CREATED)

        return Response(invitation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
