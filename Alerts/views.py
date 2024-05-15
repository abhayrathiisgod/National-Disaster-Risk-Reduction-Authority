from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import AlertList
from .serializers import AlertListSerializer
from rest_framework import filters
import django_filters
from django_ckeditor_5.fields import CKEditor5Field


class DescriptionFilter(django_filters.CharFilter):
    field_name = 'description'
    lookup_expr = 'icontains'


class AlertListView(generics.ListAPIView):
    queryset = AlertList.objects.all()
    serializer_class = AlertListSerializer
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['event', 'title', 'titleNe', 'source',
                        'polygon', 'referenceType', 'referenceData', 'region']
    search_fields = ['title', 'titleNe', 'source',
                     'polygon', 'referenceType', 'referenceData', 'region']
    ordering_fields = ['id', 'title', 'createdOn', 'expireOn', 'regionId']


class AlertInstanceView(generics.RetrieveAPIView):
    queryset = AlertList.objects.all()
    serializer_class = AlertListSerializer
    lookup_field = 'pk'
