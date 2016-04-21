from rest_framework.generics import ListAPIView
from skill.models import Skill
from skill.serializers import SkillSerializer


class SkillView(ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_queryset(self):
        queryset = Skill.objects.all()
        if 's' in self.request.query_params:
            if len(self.request.query_params['s']) > 3:
                queryset = Skill.objects.filter(name__icontains=self.request.query_params['s'])
            else:
                queryset = Skill.objects.filter(name__istartswith=self.request.query_params['s'])
        if 'limit' in self.request.query_params:
            queryset = queryset[:self.request.query_params['limit']]
        return queryset
