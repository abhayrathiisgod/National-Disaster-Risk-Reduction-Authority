from rest_framework import serializers
from galleries.models import Gallery, DisplayImage


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class DisplayImageSerializer(serializers.ModelSerializer):
    other_images = GallerySerializer(many=True)

    class Meta:
        model = DisplayImage
        fields = '__all__'
