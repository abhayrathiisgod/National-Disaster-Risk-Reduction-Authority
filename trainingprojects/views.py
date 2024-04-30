from django.shortcuts import render
from rest_framework import generics
from .serializers import ProjectDetailSerializer, ProjectListSerializer, TrainingAnalyticsSerializer, TrainingSerializer
from .models import Project, Training
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    pagination_class = None


class ProjectInstance(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    pagination_class = None
    lookup_field = 'pk'


class TrainingView(generics.ListAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    pagination_class = None
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['province', 'district', 'municipality']


class TrainingAnalyticView(generics.ListAPIView):
    queryset = Training.objects.filter(id=1)
    serializer_class = TrainingAnalyticsSerializer
    pagination_class = None
