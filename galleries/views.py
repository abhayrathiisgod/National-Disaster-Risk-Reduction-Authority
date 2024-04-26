from django.shortcuts import render
from rest_framework import generics
from galleries.models import Gallery, DisplayImage
from galleries.serializers import DisplayImageSerializer

# Create your views here.


class GalleryView(generics.ListAPIView):
    queryset = DisplayImageSerializer.objects.all()
    serializer_class = DisplayImageSerializer
    pagination_class = None
