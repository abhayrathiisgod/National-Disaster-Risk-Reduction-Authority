from django.shortcuts import render
from rest_framework import generics
from .serializers import ProjectDetailSerializer, ProjectListSerializer
from .models import Project

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
