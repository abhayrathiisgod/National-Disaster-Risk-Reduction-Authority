from django.shortcuts import render
from hazard.models import Hazards
from hazard.serializers import HazardSerializer
from rest_framework import generics, viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from .filters import HazardFilter


class HazardAPIview(viewsets.ModelViewSet):
    queryset = Hazards.objects.all().order_by('order')
    serializer_class = HazardSerializer
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['title', 'type']
    ordering_fields = ['id', 'title', 'order', 'color', 'type']
    pagination_class = LimitOffsetPagination
    filterset_class = HazardFilter
    lookup_field = 'pk'
