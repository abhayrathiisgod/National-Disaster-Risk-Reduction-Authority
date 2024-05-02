from rest_framework import viewsets, filters
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Loss, Incident
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import LossSerializer, IncidentSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination


class LossViewSet(generics.ListAPIView):
    queryset = Loss.objects.all()
    serializer_class = LossSerializer
    pagination_class = LimitOffsetPagination


class IncidentViewSet(generics.ListAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    filter_backends = [filters.SearchFilter,
                       filters.OrderingFilter, DjangoFilterBackend]

    search_fields = ['title', 'description',
                     'cause', 'streetAddress', 'region']
    ordering_fields = '__all__'
    filterset_fields = {
        'id': ['exact'],
        'title': ['exact', 'icontains'],
        'point': ['exact', 'icontains'],
        'createdOn': ['exact', 'date', 'gte', 'lte'],
        'modifiedOn': ['exact', 'date', 'gte', 'lte'],
        'titleNe': ['exact', 'icontains'],
        'verified': ['exact'],
        'approved': ['exact'],
        'incidentOn': ['exact', 'date', 'gte', 'lte'],
        'reportedOn': ['exact', 'date', 'gte', 'lte'],
        'streetAddress': ['exact', 'icontains'],
        'needFollowup': ['exact'],
        'region': ['exact', 'icontains'],
        'regionId': ['exact'],
        'dataSourceId': ['exact'],
        'dataSource': ['exact', 'icontains'],
        'source': ['exact'],
        'event': ['exact'],
        'hazard': ['exact'],
        'loss': ['exact'],
        'createdBy': ['exact'],
        'updatedBy': ['exact'],
        'wards': ['exact'],
    }

    pagination_class = LimitOffsetPagination


class IncidentInstanceSet(generics.RetrieveAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    lookup_field = 'pk'
