from rest_framework import serializers
from .models import PublicationAuthor, Publications, PublicationType


class PublicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicationType
        fields = '__all__'


class PublicationAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicationAuthor
        fields = '__all__'


class PublicationsSerializer(serializers.ModelSerializer):
    pub_type = PublicationTypeSerializer()
    pub_author = PublicationAuthorSerializer()

    class Meta:
        model = Publications
        fields = ['id', 'pub_type', 'pub_author', 'title', 'title_ne',
                  'summary', 'summary_ne', 'date', 'pdffile', 'image', 'is_published']


class PublicationsDetailSerializer(serializers.ModelSerializer):
    pub_type = PublicationTypeSerializer()
    pub_author = PublicationAuthorSerializer()

    class Meta:
        model = Publications
        fields = ['id', 'pub_type', 'pub_author', 'title', 'title_ne', 'description', 'description_ne',
                  'date', 'pdffile', 'image', 'is_published']
