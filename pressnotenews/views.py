from pressnotenews.models import NewsInfo, PressNote
from pressnotenews.serializers import ALLNewsInfoSerializer, SpecificNewsInfoSerializer, PressNoteListSerializer, PressNoteDetailSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .filters import NewsInfoFilter, PressNoteFilter


class NewsInfoViewSet(viewsets.ModelViewSet):
    queryset = NewsInfo.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_class = NewsInfoFilter
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return ALLNewsInfoSerializer
        return SpecificNewsInfoSerializer


class PressNoteAPIView(viewsets.ModelViewSet):
    queryset = PressNote.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_class = PressNoteFilter
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return PressNoteListSerializer
        return PressNoteDetailSerializer
