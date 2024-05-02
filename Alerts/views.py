from rest_framework import generics
from django.db.models import Q
from .models import AlertList
from .serializers import AlertListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class AlertListView(generics.ListAPIView):
    queryset = AlertList.objects.all().order_by('id')
    serializer_class = AlertListSerializer
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['event', 'title', 'titleNe', 'source', 'description',
                        'polygon', 'referenceType', 'referenceData', 'region']
    search_fields = ['title', 'titleNe', 'source', 'description',
                     'polygon', 'referenceType', 'referenceData', 'region']
    ordering_fields = ['id', 'title', 'createdOn', 'expireOn', 'regionId']
    ordering = ['id']


class AlertInstanceView(generics.ListAPIView):
    queryset = AlertList.objects.all()
    serializer_class = AlertListSerializer
    lookup_field = 'pk'
