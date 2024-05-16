from django.shortcuts import render
from rest_framework import generics, viewsets
from federal.models import Province, District, Municipality, Ward
from federal.serializers import ProvinceSerializer, DistrictSerializer, MunicipalitySerializer, WardSerializer, WardDetailSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from .filters import DistrictFilter


class ProvinceView(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['id', 'province_name']
    pagination_class = LimitOffsetPagination
    lookup_field = 'pk'


class DistrictView(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['id', 'district_name']
    pagination_class = LimitOffsetPagination
    filterset_class = DistrictFilter
    lookup_field = 'pk'


class MunicipalityView(viewsets.ModelViewSet):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['id', 'municipality_name']
    pagination_class = LimitOffsetPagination
    lookup_field = 'pk'


class WardView(viewsets.ModelViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['id', 'ward_name']
    pagination_class = LimitOffsetPagination
    lookup_field = 'pk'
