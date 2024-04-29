from rest_framework import serializers
from .models import ContactDetail, Introduction, WardDocument, FrequentlyAskedQuestions, Page


class ContactDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetail
        fields = '__all__'


class IntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction
        fields = '__all__'


class WardDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardDocument
        fields = '__all__'


class FrequentlyAskedQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentlyAskedQuestions
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'
