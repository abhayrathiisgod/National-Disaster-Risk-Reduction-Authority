from rest_framework import serializers
from .models import Skills, Designation, Department, TrainingOrg, TrainingCertificate, Trainings, OfficerProfile, CommiteProfile, NationalCouncilHead, ExecutiveCommitteHead, OfficersHead, OfficersSpokesPerson, InformationOfficer


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class TrainingOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingOrg
        fields = '__all__'


class TrainingCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingCertificate
        fields = '__all__'


class TrainingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainings
        fields = '__all__'


class OfficerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficerProfile
        fields = '__all__'


class CommiteProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommiteProfile
        fields = '__all__'


class NationalCouncilHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = NationalCouncilHead
        fields = '__all__'


class ExecutiveCommitteHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutiveCommitteHead
        fields = '__all__'


class OfficersHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficersHead
        fields = '__all__'


class OfficersSpokesPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficersSpokesPerson
        fields = '__all__'


class InformationOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationOfficer
        fields = '__all__'
