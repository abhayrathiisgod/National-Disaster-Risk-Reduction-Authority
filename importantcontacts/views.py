from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from importantcontacts.models import ProvinceWiseFocalPersonContactList, DeocHeadList, LocalDisasterManagementContactList, MohaSubordinateList, MohaPhoneDirectoryList, SnakeBites, EmergencyVehicle
from importantcontacts.serializers import ProvinceWiseFocalPersonContactSerializer, DeocHeadSerializer, LocalDisasterManagementContactSerializer, MohaSubordinateSerializer, MohaPhoneDirectorySerializer, SnakeBiteSerializer, AmbulanceSerializer, FireTruckSerializer
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.


class ProvinceWiseFocalPersonContactListView(generics.ListAPIView):
    queryset = ProvinceWiseFocalPersonContactList.objects.all()
    serializer_class = ProvinceWiseFocalPersonContactSerializer
    pagination_class = LimitOffsetPagination


class DeocHeadView(generics.ListAPIView):
    queryset = DeocHeadList.objects.all()
    serializer_class = DeocHeadSerializer
    pagination_class = LimitOffsetPagination


class LocalDisasterManagementContactView(generics.ListAPIView):
    queryset = LocalDisasterManagementContactList.objects.all()
    serializer_class = LocalDisasterManagementContactSerializer
    pagination_class = LimitOffsetPagination


class MohaSubordinateView(generics.ListAPIView):
    queryset = MohaSubordinateList.objects.all()
    serializer_class = MohaSubordinateSerializer
    pagination_class = LimitOffsetPagination


class MohaPhoneDirectoryView(generics.ListAPIView):
    queryset = MohaPhoneDirectoryList.objects.all()
    serializer_class = MohaPhoneDirectorySerializer
    pagination_class = LimitOffsetPagination


class SnakeBitesView(generics.ListAPIView):
    queryset = SnakeBites.objects.all()
    serializer_class = SnakeBiteSerializer
    pagination_class = LimitOffsetPagination


class AmbulanceView(generics.ListAPIView):
    queryset = EmergencyVehicle.objects.filter(vehicle_type='Ambulance')
    serializer_class = AmbulanceSerializer
    pagination_class = LimitOffsetPagination


class FireTruckView(generics.ListAPIView):
    queryset = EmergencyVehicle.objects.filter(vehicle_type='Fire_truck')
    serializer_class = FireTruckSerializer
    pagination_class = LimitOffsetPagination
