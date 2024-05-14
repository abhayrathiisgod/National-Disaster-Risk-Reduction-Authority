from django.shortcuts import render
from rest_framework import generics
from galleries.models import Gallery, GalleryImage, VideoGallery
from galleries.serializers import GalleryDetailSerializer, GalleryImageSerializer, GallerySerializer, VideoGallerySerializer
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.


class GalleryView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    pagination_class = LimitOffsetPagination


class GalleryDetailView(generics.RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GalleryDetailSerializer
    pagination_class = None
    lookup_field = 'pk'


class VideoGalleryView(generics.ListAPIView):
    queryset = VideoGallery.objects.all()
    serializer_class = VideoGallerySerializer
    pagination_class = LimitOffsetPagination


class VideoGalleryDetailView(generics.RetrieveAPIView):
    queryset = VideoGallery.objects.all()
    serializer_class = VideoGallerySerializer
    pagination_class = None
    lookup_field = 'pk'
