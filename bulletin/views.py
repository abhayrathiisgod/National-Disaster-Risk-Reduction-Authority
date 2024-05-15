from django.shortcuts import render
from rest_framework import generics
from bulletin.models import Bulletin
from bulletin.serializers import BulletinSerializer
from bulletin.pagination import PaginationClass
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

# need 3 types of views
# 1. returns all
# 2. return only national
# 3. returns date wise descending


# viewsets
class BulletinList(generics.ListAPIView):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer
    pagination_class = PaginationClass
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['bulletin_type']


##
class BulletindailylList(generics.ListAPIView):
    queryset = Bulletin.objects.filter(bulletin_type__id=1)
    serializer_class = BulletinSerializer
    pagination_class = PaginationClass

##


class BulletinNationalList(generics.ListAPIView):
    queryset = Bulletin.objects.filter(bulletin_type__id=2)
    serializer_class = BulletinSerializer
    pagination_class = PaginationClass


class BulletinDateWiseList(generics.ListAPIView):
    queryset = Bulletin.objects.all().order_by('-date')
    serializer_class = BulletinSerializer
    pagination_class = PaginationClass
