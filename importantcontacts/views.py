from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from importantcontacts.models import ProvinceWiseFocalPersonContactList, DeocHeadList, LocalDisasterManagementContactList, MohaSubordinateList, MohaPhoneDirectoryList, SnakeBites, EmergencyVehicle
from importantcontacts.serializers import ProvinceWiseFocalPersonContactSerializer, DeocHeadSerializer, LocalDisasterManagementContactSerializer, MohaSubordinateSerializer, MohaPhoneDirectorySerializer, SnakeBiteSerializer, AmbulanceSerializer, FireTruckSerializer
from importantcontacts.pagination import PaginationClass
# Create your views here.


class ProvinceWiseFocalPersonContactListView(generics.ListAPIView):
    queryset = ProvinceWiseFocalPersonContactList.objects.all()
    serializer_class = ProvinceWiseFocalPersonContactSerializer
    pagination_class = PaginationClass


class DeocHeadView(generics.ListAPIView):
    queryset = DeocHeadList.objects.all()
    serializer_class = DeocHeadSerializer
    pagination_class = PaginationClass


class LocalDisasterManagementContactView(generics.ListAPIView):
    queryset = LocalDisasterManagementContactList.objects.all()
    serializer_class = LocalDisasterManagementContactSerializer
    pagination_class = PaginationClass


class MohaSubordinateView(generics.ListAPIView):
    queryset = MohaSubordinateList.objects.all()
    serializer_class = MohaSubordinateSerializer
    pagination_class = PaginationClass


class MohaPhoneDirectoryView(generics.ListAPIView):
    queryset = MohaPhoneDirectoryList.objects.all()
    serializer_class = MohaPhoneDirectorySerializer
    pagination_class = PaginationClass


class SnakeBitesView(generics.ListAPIView):
    queryset = SnakeBites.objects.all()
    serializer_class = SnakeBiteSerializer
    pagination_class = PaginationClass


class AmbulanceView(generics.ListAPIView):
    queryset = EmergencyVehicle.objects.filter(vehicle_type='Ambulance')
    serializer_class = AmbulanceSerializer
    pagination_class = PaginationClass


class FireTruckView(generics.ListAPIView):
    queryset = EmergencyVehicle.objects.filter(vehicle_type='Fire_truck')
    serializer_class = FireTruckSerializer
    pagination_class = PaginationClass
