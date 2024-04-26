from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from importantcontacts.models import ProvinceWiseFocalPersonContactList, DeocHeadList, LocalDisasterManagementContactList, MohaSubordinateList, MohaPhoneDirectoryList
from importantcontacts.serializers import ProvinceWiseFocalPersonContactSerializer, DeocHeadSerializer, LocalDisasterManagementContactSerializer, MohaSubordinateSerializer, MohaPhoneDirectorySerializer
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
