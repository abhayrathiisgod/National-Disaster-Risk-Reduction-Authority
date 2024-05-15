from django.shortcuts import render
from rest_framework import generics
from .models import Publications
from .serializers import PublicationsSerializer, PublicationsDetailSerializer
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class Allpublicationview(generics.ListAPIView):
    queryset = Publications.objects.all()
    serializer_class = PublicationsSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pub_type']


class PublicationDetailView(generics.RetrieveAPIView):
    queryset = Publications.objects.all()
    serializer_class = PublicationsDetailSerializer
    lookup_field = 'slug'
