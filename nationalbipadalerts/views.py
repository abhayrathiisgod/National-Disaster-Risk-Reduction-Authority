from django.shortcuts import render
from rest_framework import generics
from .models import BipadAlerts
from .serializers import BipadAlertsSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
# from .filters import BipadAlertsFilter
# Create your views here.


class ImportantLinksList(generics.ListAPIView):
    pass


class BipadAlertsList(generics.ListAPIView):
    queryset = BipadAlerts.objects.all()
    serializer_class = BipadAlertsSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['last_updated']
    pagination_class = LimitOffsetPagination


class BipadAlertView(generics.RetrieveAPIView):
    queryset = BipadAlerts.objects.all()
    serializer_class = BipadAlertsSerializer
    lookup_field = 'pk'
    # pagination_class = LimitOffsetPagination
