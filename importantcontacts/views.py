from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from importantcontacts.models import ProvinceWiseFocalPersonContactList, DeocHeadList, LocalDisasterManagementContactList, MohaSubordinateList, MohaPhoneDirectoryList, SnakeBites, EmergencyVehicle
from importantcontacts.serializers import ProvinceWiseFocalPersonContactSerializer, DeocHeadSerializer, LocalDisasterManagementContactSerializer, MohaSubordinateSerializer, MohaPhoneDirectorySerializer, SnakeBiteSerializer,  EmergencyVehicleSerializer
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.
from rest_framework import viewsets, filters
from .filters import EmergencyVehicleFilter


class ProvinceWiseFocalPersonContactViewSet(viewsets.ModelViewSet):
    queryset = ProvinceWiseFocalPersonContactList.objects.all()
    serializer_class = ProvinceWiseFocalPersonContactSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['province']
    lookup_field = 'pk'


class DeocHeadViewSet(viewsets.ModelViewSet):
    queryset = DeocHeadList.objects.all()
    serializer_class = DeocHeadSerializer
    pagination_class = LimitOffsetPagination


class LocalDisasterManagementContactViewSet(viewsets.ModelViewSet):
    queryset = LocalDisasterManagementContactList.objects.all()
    serializer_class = LocalDisasterManagementContactSerializer
    pagination_class = LimitOffsetPagination


class MohaSubordinateViewSet(viewsets.ModelViewSet):
    queryset = MohaSubordinateList.objects.all()
    serializer_class = MohaSubordinateSerializer
    pagination_class = LimitOffsetPagination


class MohaPhoneDirectoryViewSet(viewsets.ModelViewSet):
    queryset = MohaPhoneDirectoryList.objects.all()
    serializer_class = MohaPhoneDirectorySerializer
    pagination_class = LimitOffsetPagination


class SnakeBitesViewSet(viewsets.ModelViewSet):
    queryset = SnakeBites.objects.all()
    serializer_class = SnakeBiteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['district']
    pagination_class = LimitOffsetPagination


class EmergencyVehicleViewSet(viewsets.ModelViewSet):
    queryset = EmergencyVehicle.objects.all()
    serializer_class = EmergencyVehicleSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = EmergencyVehicleFilter
