from django.shortcuts import render
from rest_framework import generics, viewsets
from guidecourse.models import GuideCourse, Guidechildren
from guidecourse.serializers import GuideCourseSerializer, GuidechildrenSerializer, CourseDetailSerializer, CourseSerializer
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.


from rest_framework import generics
from .models import GuideCourse, Course
from .serializers import GuideCourseSerializer, GuideListSerializer


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = LimitOffsetPagination
    lookup_field = 'pk'


class GuideListView(generics.ListAPIView):
    queryset = GuideCourse.objects.all()
    serializer_class = GuideListSerializer
    pagination_class = LimitOffsetPagination


class GuideCourseView(viewsets.ModelViewSet):
    queryset = GuideCourse.objects.all()
    serializer_class = GuideCourseSerializer
    pagination_class = LimitOffsetPagination
    lookup_field = 'pk'
