from django.shortcuts import render
from rest_framework import generics
from galleries.models import Gallery, GalleryImage, VideoGallery
from galleries.serializers import GalleryImageSerializer, GallerySerializer, VideoGallerySerializer

# Create your views here.


class GalleryView(generics.ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    pagination_class = None


class GalleryDetailView(generics.RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    pagination_class = None
    lookup_field = 'pk'


class VideoGalleryView(generics.ListAPIView):
    queryset = VideoGallery.objects.all()
    serializer_class = VideoGallerySerializer
    pagination_class = None


class VideoGalleryDetailView(generics.RetrieveAPIView):
    queryset = VideoGallery.objects.all()
    serializer_class = VideoGallerySerializer
    pagination_class = None
    lookup_field = 'pk'
