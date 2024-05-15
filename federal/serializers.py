from rest_framework import serializers
from .models import Province, District, Municipality, Ward


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'province_name', 'province_name_ne', 'code']


class DistrictSerializer(serializers.ModelSerializer):
    # province = ProvinceSerializer()

    class Meta:
        model = District
        fields = ['id', 'district_name', 'district_name_ne',
                  'code', 'province']


class MunicipalitySerializer(serializers.ModelSerializer):
    province = ProvinceSerializer(read_only=True)
    district = DistrictSerializer(read_only=True)

    class Meta:
        model = Municipality
        fields = ['id', 'municipality_name', 'municipality_name_ne',
                  'province', 'district']


class WardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ward
        fields = ['id', 'ward_name', 'ward_name_ne', 'province',
                  'district', 'municipality']


class DistrictWSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = ['id', 'district_name', 'district_name_ne',
                  'code', 'province']


class MunicipalityWSerializer(serializers.ModelSerializer):

    class Meta:
        model = Municipality
        fields = ['id', 'municipality_name', 'municipality_name_ne',
                  'province', 'district']


class WardDetailSerializer(serializers.ModelSerializer):
    province = ProvinceSerializer()
    district = DistrictWSerializer()
    municipality = MunicipalityWSerializer()

    class Meta:
        model = Ward
        fields = ['id', 'ward_name', 'ward_name_ne', 'province',
                  'district', 'municipality']
