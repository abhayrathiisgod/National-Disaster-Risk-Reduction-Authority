from .models import Publications
from .serializers import PublicationsSerializer, PublicationsDetailSerializer
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .filters import PublicationsFilter


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publications.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = PublicationsFilter
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PublicationsDetailSerializer
        return PublicationsSerializer
