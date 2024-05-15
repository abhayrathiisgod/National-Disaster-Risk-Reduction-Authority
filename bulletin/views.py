from bulletin.models import Bulletin
from bulletin.serializers import BulletinSerializer, BulletinDetailSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from .filters import BulletinFilter


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 4


class BulletinViewSets(viewsets.ModelViewSet):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer
    filterset_class = BulletinFilter
    pagination_class = CustomLimitOffsetPagination

    def retrieve(self, request, slug=None):
        queryset = self.get_queryset()
        bulletin = get_object_or_404(queryset, slug=slug)
        serializer = BulletinDetailSerializer(bulletin)
        return Response(serializer.data)
