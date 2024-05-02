from rest_framework import serializers
from .models import GuideCourse, Guidechildren, Course


class GuidechildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guidechildren
        fields = ['id', 'name', 'name_ne', 'title', 'title_ne',
                  'description', 'description_ne', 'image']


class GuideListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuideCourse
        fields = ['id', 'title', 'title_ne', 'image']


class GuideCourseSerializer(serializers.ModelSerializer):
    more_detail = GuidechildrenSerializer(many=True, read_only=True)

    class Meta:
        model = GuideCourse
        fields = ['id', 'name', 'title', 'title_ne',
                  'description', 'description_ne', 'image', 'more_detail']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'title_ne', 'image',
                  'skill_level', ]


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'title_ne', 'path', 'image', 'youtube_url', 'description', 'description_ne',
                  'target_audience', 'target_audience_ne', 'duration', 'skill_level', 'language', 'learning_objective', 'learning_objective_ne']
