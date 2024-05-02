from django.shortcuts import render
from rest_framework import generics
from federal.models import Province, District, Municipality, Ward
from federal.serializers import ProvinceSerializer, DistrictSerializer, MunicipalitySerializer, WardSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.


class ProvinceView(generics.ListAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['id', 'province_name']
    pagination_class = LimitOffsetPagination


class ProvinceInstanceView(generics.RetrieveAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    lookup_field = 'pk'


class DistrictView(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['id', 'district_name']
    pagination_class = LimitOffsetPagination


class DistrictInstanceView(generics.RetrieveAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    lookup_field = 'pk'


class MunicipalityView(generics.ListAPIView):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['id', 'municipality_name']
    pagination_class = LimitOffsetPagination


class MunicipalityInstanceView(generics.RetrieveAPIView):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    lookup_field = 'pk'


class WardView(generics.ListAPIView):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['id', 'ward_name']
    pagination_class = LimitOffsetPagination


class WardInstanceView(generics.RetrieveAPIView):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
    lookup_field = 'pk'
