from rest_framework import serializers
from .models import Address, Donater, Project, Training
from federal.serializers import DistrictSerializer
from datetime import date


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class DonaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donater
        fields = '__all__'


class ProjectListSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    # donor = DonaterSerializer()
    district = DistrictSerializer()

    class Meta:
        model = Project
        fields = ['id', 'address', 'created_at', 'updated_at', 'deleted_at', 'title', 'title_ne',
                  'budget', 'budget_ne', 'start_date', 'end_date', 'created_by', 'updated_by', 'district']


class ProjectDetailSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    donor = DonaterSerializer()
    district = DistrictSerializer()

    class Meta:
        model = Project
        fields = ['id', 'address', 'donor', 'created_at', 'updated_at', 'deleted_at', 'title', 'title_ne',
                  'budget', 'budget_ne', 'start_date', 'end_date', 'created_by', 'updated_by', 'district']


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'


class TrainingAnalyticsSerializer(serializers.Serializer):
    total_count = serializers.SerializerMethodField()
    today = serializers.SerializerMethodField()
    total_ongoing = serializers.SerializerMethodField()
    total_complete = serializers.SerializerMethodField()
    municipality_covered = serializers.SerializerMethodField()

    def get_total_count(self, obj):
        return Training.objects.count()

    def get_today(self, obj):
        return date.today()

    def get_total_ongoing(self, obj):
        today = date.today()
        return Training.objects.filter(endDate__lt=today).count()

    def get_total_complete(self, obj):
        today = date.today()
        return Training.objects.filter(endDate__gt=today).count()

    def get_municipality_covered(self, obj):
        return Training.objects.exclude(municipality__isnull=True).count()
