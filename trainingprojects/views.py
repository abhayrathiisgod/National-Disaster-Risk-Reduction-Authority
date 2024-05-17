from django.shortcuts import render
from rest_framework import generics
from .serializers import ProjectDetailSerializer, ProjectListSerializer, TrainingListSerializer, TrainingAnalyticsSerializer, TrainingSerializer, GeoHazardAssessmentSerializer
from .models import Project, Training, GeoHazardAssessment
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets


class ProjectListView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['province', 'district', 'municipality']
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        return ProjectDetailSerializer


class TrainingView(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['province', 'district', 'municipality']
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.action == 'list':
            return TrainingListSerializer
        return TrainingSerializer


class TrainingAnalyticView(generics.ListAPIView):
    queryset = Training.objects.filter(id=1)
    serializer_class = TrainingAnalyticsSerializer
    pagination_class = None


class GeoHazardView(viewsets.ModelViewSet):
    queryset = GeoHazardAssessment.objects.all()
    serializer_class = GeoHazardAssessmentSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['province', 'district', 'municipality']
    lookup_field = 'pk'
