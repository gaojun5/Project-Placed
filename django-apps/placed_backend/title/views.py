from rest_framework.generics import ListAPIView
from title.models import Title
from title.serializers import TitleSerializer


class TitleListView(ListAPIView):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

    def get_queryset(self):
        group_id = self.kwargs['group_id']
        return Title.objects.filter(group__id=group_id)
