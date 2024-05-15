from rest_framework import serializers
from .models import Gallery, GalleryImage, VideoGallery


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'title', 'title_ne', 'photo_credit',
                  'photo_credit_ne', 'caption', 'caption_ne', 'image']


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'title', 'title_ne', 'image']


class GalleryDetailSerializer(serializers.ModelSerializer):
    images = GalleryImageSerializer(many=True)

    class Meta:
        model = Gallery
        fields = ['id', 'title', 'title_ne', 'image', 'images']


class VideoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGallery
        fields = ['id', 'youtube_url']
