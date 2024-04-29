from rest_framework import serializers
from .models import Gallery, GalleryImage, VideoGallery


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    images = GalleryImageSerializer(many=True)

    class Meta:
        model = Gallery
        fields = ['id', 'title', 'title_ne', 'image', 'images']


class GalleryDetailSerializer(serializers.ModelSerializer):
    images = GalleryImageSerializer(many=True)

    class Meta:
        model = Gallery
        fields = ['id', 'title', 'title_ne', 'image', 'images']


class VideoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGallery
        fields = '__all__'
