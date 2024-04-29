from django.shortcuts import render
from rest_framework import generics
from guidecourse.models import GuideCourse, Guidechildren
from guidecourse.serializers import GuideCourseSerializer, GuidechildrenSerializer, CourseDetailSerializer, CourseSerializer

# Create your views here.


from rest_framework import generics
from .models import GuideCourse, Course
from .serializers import GuideCourseSerializer, GuideListSerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseInstance(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    lookup_field = 'pk'


class GuideListView(generics.ListAPIView):
    queryset = GuideCourse.objects.all()
    serializer_class = GuideListSerializer


class GuideCourseView(generics.ListAPIView):
    queryset = GuideCourse.objects.all()
    serializer_class = GuideCourseSerializer


class GuideCourseDetailView(generics.RetrieveAPIView):
    serializer_class = GuideCourseSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = GuideCourse.objects.filter(id=pk)
        return queryset
