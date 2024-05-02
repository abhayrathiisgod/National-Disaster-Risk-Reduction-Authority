from django.shortcuts import render
from pressnotenews.models import NewsInfo, PressNote
from rest_framework import generics
from pressnotenews.serializers import ALLNewsInfoSerializer, SpecificNewsInfoSerializer, PressNoteSerializer
# Create your views here.
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination


class NewsInfoViewsetList(generics.ListAPIView):
    queryset = NewsInfo.objects.all()
    serializer_class = ALLNewsInfoSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['date']
    pagination_class = LimitOffsetPagination


class NewsInfoViewsetInstance(generics.ListAPIView):
    serializer_class = SpecificNewsInfoSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = NewsInfo.objects.filter(id=pk)
        return queryset


class PressNoteListAPIView(generics.ListAPIView):
    queryset = PressNote.objects.all()
    serializer_class = PressNoteSerializer
    pagination_class = LimitOffsetPagination


class PressNoteAPIView(generics.RetrieveAPIView):
    queryset = PressNote.objects.all()
    serializer_class = PressNoteSerializer
    lookup_field = 'pk'
