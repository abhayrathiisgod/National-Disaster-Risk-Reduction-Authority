from django.shortcuts import render
from hazard.models import Hazards
from hazard.serializers import HazardSerializer
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.


class HazardList(generics.ListAPIView):
    queryset = Hazards.objects.all().order_by('order')
    serializer_class = HazardSerializer
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['id', 'title', 'order', 'color', 'type']
    pagination_class = LimitOffsetPagination


class HazardInstance(generics.RetrieveAPIView):
    queryset = Hazards.objects.all()
    serializer_class = HazardSerializer
    lookup_field = 'pk'
