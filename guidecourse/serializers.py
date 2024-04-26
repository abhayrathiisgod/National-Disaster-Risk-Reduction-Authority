from rest_framework import serializers
from guidecourse.models import GuideCourse, GuideChildren


class GuideChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideChildren
        fields = ['id', 'name', 'name_ne', 'title',
                  'title_ne', 'description', 'description_ne']


class GuideCourseSerializer(serializers.ModelSerializer):
    children = GuideChildrenSerializer(many=True, read_only=True)

    class Meta:
        model = GuideCourse
        fields = ['id', 'name', 'title', 'title_ne',
                  'description', 'description_ne', 'image', 'children']
