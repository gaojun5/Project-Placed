from rest_framework import viewsets
from course_module.models import CourseModule
from course_module.serializers import CourseModuleSerializer, CourseModuleCreateSerializer


class CourseModuleViewSet(viewsets.ModelViewSet):
    queryset = CourseModule.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CourseModuleCreateSerializer
        return CourseModuleSerializer
