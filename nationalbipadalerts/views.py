from django.shortcuts import render
from rest_framework import generics
from .models import BipadAlerts
from .serializers import BipadAlertsSerializer, BipadAlertsListSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets


class ImportantLinksList(generics.ListAPIView):
    pass


class BipadAlertsView(viewsets.ModelViewSet):
    queryset = BipadAlerts.objects.all()
    serializer_class = BipadAlertsSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['last_updated']
    pagination_class = LimitOffsetPagination
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.action == 'list':
            return BipadAlertsListSerializer
        elif self.action == 'retrieve':
            return BipadAlertsSerializer
