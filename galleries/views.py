from django.shortcuts import render
from rest_framework import generics, viewsets
from galleries.models import Gallery, GalleryImage, VideoGallery
from galleries.serializers import GalleryDetailSerializer, GalleryImageSerializer, GallerySerializer, VideoGallerySerializer
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.


class GalleryView(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    pagination_class = LimitOffsetPagination
    lookup_field = 'pk'


class VideoGalleryView(viewsets.ModelViewSet):
    queryset = VideoGallery.objects.all()
    serializer_class = VideoGallerySerializer
    pagination_class = LimitOffsetPagination
    lookup_field = 'pk'
