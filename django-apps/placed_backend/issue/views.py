from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from issue.models import Issue
from issue.serializers import IssueSerializer


class IssueViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.filter(to=self.request.user)
