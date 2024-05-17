from rest_framework import serializers
from pressnotenews.models import NewsInfo, Author, Type, PressNote


class ALLNewsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsInfo
        fields = ['id', 'title', 'title_ne', 'slug',
                  'summary', 'summary_ne', 'date', 'image']


class SpecificNewsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsInfo
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['Author_id', 'name', 'name_ne']


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['Type_id', 'name', 'name_ne']


class PressNoteListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PressNote
        fields = ['id', 'title', 'title_ne', 'slug',
                  'summary', 'summary_ne', 'date', 'image', 'is_published']


class PressNoteDetailSerializer(serializers.ModelSerializer):
    author_details = AuthorSerializer(source='author', read_only=True)
    type_details = TypeSerializer(source='type', read_only=True)

    class Meta:
        model = PressNote
        fields = ['id', 'title', 'title_ne', 'slug', 'description', 'description_ne',
                  'summary', 'summary_ne', 'date', 'image', 'file', 'is_published', 'author_details', 'type_details']
