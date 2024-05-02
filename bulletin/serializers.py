from rest_framework import serializers
from bulletin.models import Bulletin, BulletinAuthor, BulletinType


class BulletinAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulletinAuthor
        fields = ['id', 'author', 'author_ne']


class BulletinTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulletinType
        fields = ['id', 'bulletin_type', 'bulletin_type_ne']


class BulletinSerializer(serializers.ModelSerializer):
    bulletin_author = BulletinAuthorSerializer()
    bulletin_type = BulletinTypeSerializer()

    class Meta:
        model = Bulletin
        fields = ['id', 'bulletin_author', 'bulletin_type', 'title',
                  'title_ne', 'summary', 'summary_ne', 'date', 'image']
