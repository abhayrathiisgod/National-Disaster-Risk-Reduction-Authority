from django.shortcuts import render
from pressnotenews.models import NewsInfo, PressNote
from rest_framework import generics
from pressnotenews.serializers import ALLNewsInfoSerializer, SpecificNewsInfoSerializer, PressNoteSerializer
# Create your views here.
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets
from rest_framework.filters import SearchFilter


class NewsInfoViewSet(viewsets.ModelViewSet):
    queryset = NewsInfo.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['date']
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return ALLNewsInfoSerializer
        elif self.action == 'retrieve':
            return SpecificNewsInfoSerializer
        return ALLNewsInfoSerializer


class PressNoteAPIView(viewsets.ModelViewSet):
    queryset = PressNote.objects.all()
    serializer_class = PressNoteSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['date']
    lookup_field = 'pk'
