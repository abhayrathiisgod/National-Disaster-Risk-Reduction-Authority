from rest_framework import serializers
from importantcontacts.models import ProvinceWiseFocalPersonContactList, DeocHeadList, LocalDisasterManagementContactList, MohaSubordinateList, MohaPhoneDirectoryList


class ProvinceWiseFocalPersonContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvinceWiseFocalPersonContactList
        fields = '__all__'


class DeocHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeocHeadList
        fields = '__all__'


class LocalDisasterManagementContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalDisasterManagementContactList
        fields = '__all__'


class MohaSubordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MohaSubordinateList
        fields = '__all__'


class MohaPhoneDirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MohaPhoneDirectoryList
        fields = '__all__'
