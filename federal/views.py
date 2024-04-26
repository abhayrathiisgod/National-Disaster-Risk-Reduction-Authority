from django.shortcuts import render
from rest_framework import generics
from federal.models import Province, District, Municipality, Ward
from federal.serializers import ProvinceSerializer, DistrictSerializer, MunicipalitySerializer, WardSerializer
from federal.pagination import PaginationClass

# Create your views here.


class ProvinceView(generics.ListAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    pagination_class = PaginationClass


class DistrictView(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    pagination_class = PaginationClass


class MunicipalityView(generics.ListAPIView):
    queryset = Municipality.objects.all()
    serializer_class = MunicipalitySerializer
    pagination_class = PaginationClass


class WardView(generics.ListAPIView):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
    pagination_class = PaginationClass
