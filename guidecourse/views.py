from django.shortcuts import render
from rest_framework import generics
from guidecourse.models import GuideCourse, GuideChildren
from guidecourse.serializers import GuideChildrenSerializer, GuideCourseSerializer

# Create your views here.


class GuideCourseView(generics.ListAPIView):
    queryset = GuideCourse.objects.all()
    serializer_class = GuideCourseSerializer
    pagination_class = None
    # lookup_field = 'name'


class GuideCourseDetailView(generics.ListAPIView):
    queryset = GuideCourse.objects.all()
    serializer_class = GuideCourseSerializer
    pagination_class = None
    lookup_field = 'name'
