from rest_framework import generics
from rest_framework.views import APIView
from .models import Skills, Designation, Department, TrainingOrg, TrainingCertificate, Trainings, OfficerProfile, CommiteProfile, NationalCouncilHead, ExecutiveCommitteHead, OfficersHead, OfficersSpokesPerson, InformationOfficer
from profiles.serializers import SkillsSerializer, DesignationSerializer, DepartmentSerializer, TrainingOrgSerializer, TrainingCertificateSerializer, TrainingsSerializer, OfficerProfileSerializer, CommiteProfileSerializer, NationalCouncilHeadSerializer, ExecutiveCommitteHeadSerializer, OfficersHeadSerializer, OfficersSpokesPersonSerializer, InformationOfficerSerializer
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination


class SkillsListAPIView(generics.ListAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    pagination_class = LimitOffsetPagination


class SkillsAPIView(generics.RetrieveAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    lookup_field = 'pk'


class DesignationListAPIView(generics.ListAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    pagination_class = LimitOffsetPagination


class DesignationAPIView(generics.RetrieveAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    lookup_field = 'pk'


class DepartmentListAPIView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    pagination_class = LimitOffsetPagination


class DepartmentAPIView(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'pk'


class TrainingOrgListAPIView(generics.ListAPIView):
    queryset = TrainingOrg.objects.all()
    serializer_class = TrainingOrgSerializer
    pagination_class = LimitOffsetPagination


class TrainingOrgAPIView(generics.RetrieveAPIView):
    queryset = TrainingOrg.objects.all()
    serializer_class = TrainingOrgSerializer
    lookup_field = 'pk'


class TrainingCertificateListAPIView(generics.ListAPIView):
    queryset = TrainingCertificate.objects.all()
    serializer_class = TrainingCertificateSerializer
    pagination_class = LimitOffsetPagination


class TrainingCertificateAPIView(generics.RetrieveAPIView):
    queryset = TrainingCertificate.objects.all()
    serializer_class = TrainingCertificateSerializer
    lookup_field = 'pk'


class TrainingsListAPIView(generics.ListAPIView):
    queryset = Trainings.objects.all()
    serializer_class = TrainingsSerializer
    pagination_class = LimitOffsetPagination


class TrainingsAPIView(generics.RetrieveAPIView):
    queryset = Trainings.objects.all()
    serializer_class = TrainingsSerializer
    lookup_field = 'pk'


class OfficerProfileListAPIView(generics.ListAPIView):
    queryset = OfficerProfile.objects.all().order_by('order')
    serializer_class = OfficerProfileSerializer
    pagination_class = LimitOffsetPagination


class OfficerProfileAPIView(generics.RetrieveAPIView):
    queryset = OfficerProfile.objects.all()
    serializer_class = OfficerProfileSerializer
    lookup_field = 'pk'


class CommiteProfileListAPIView(generics.ListAPIView):
    queryset = CommiteProfile.objects.all().order_by('order')
    serializer_class = CommiteProfileSerializer
    pagination_class = LimitOffsetPagination


class CommiteProfileInstanceView(generics.RetrieveAPIView):
    queryset = CommiteProfile.objects.all()
    serializer_class = CommiteProfileSerializer
    lookup_field = 'pk'


class NationalCouncilHeadListAPIView(generics.ListAPIView):
    queryset = NationalCouncilHead.objects.all().order_by('order')
    serializer_class = NationalCouncilHeadSerializer
    pagination_class = LimitOffsetPagination


class NationalCouncilHeadAPIView(generics.RetrieveAPIView):
    queryset = NationalCouncilHead.objects.all()
    serializer_class = NationalCouncilHeadSerializer
    lookup_field = 'pk'


class ExecutiveCommitteHeadListAPIView(generics.ListAPIView):
    queryset = ExecutiveCommitteHead.objects.all().order_by('order')
    serializer_class = ExecutiveCommitteHeadSerializer
    pagination_class = LimitOffsetPagination


class ExecutiveCommitteHeadAPIView(generics.RetrieveAPIView):
    queryset = ExecutiveCommitteHead.objects.all()
    serializer_class = ExecutiveCommitteHeadSerializer
    lookup_field = 'pk'


class OfficersHeadListAPIView(generics.ListAPIView):
    queryset = OfficersHead.objects.all().order_by('order')
    serializer_class = OfficersHeadSerializer
    pagination_class = LimitOffsetPagination


class OfficersHeadAPIView(generics.RetrieveAPIView):
    queryset = OfficersHead.objects.all()
    serializer_class = OfficersHeadSerializer
    lookup_field = 'pk'


class OfficersSpokesPersonListAPIView(generics.ListAPIView):
    queryset = OfficersSpokesPerson.objects.all().order_by('order')
    serializer_class = OfficersSpokesPersonSerializer
    pagination_class = LimitOffsetPagination


class OfficersSpokesPersonAPIView(generics.RetrieveAPIView):
    queryset = OfficersSpokesPerson.objects.all()
    serializer_class = OfficersSpokesPersonSerializer
    lookup_field = 'pk'


class InformationOfficerListAPIView(generics.ListAPIView):
    queryset = InformationOfficer.objects.all().order_by('order')
    serializer_class = InformationOfficerSerializer
    pagination_class = LimitOffsetPagination


class InformationOfficerAPIView(generics.RetrieveAPIView):
    queryset = InformationOfficer.objects.all()
    serializer_class = InformationOfficerSerializer
    lookup_field = 'pk'


class OfficerProfileView(generics.ListAPIView):
    queryset = OfficerProfile.objects.all().order_by('order')
    serializer_class = OfficerProfileSerializer
    pagination_class = LimitOffsetPagination


class OfficerProfileInstanceView(generics.RetrieveAPIView):
    queryset = OfficerProfile.objects.all()
    serializer_class = OfficerProfileSerializer
    lookup_field = 'pk'


class CouncilProfileView(APIView):
    def get(self, request, *args, **kwargs):

        national_council_head = NationalCouncilHead.objects.first()
        executive_committe_head = ExecutiveCommitteHead.objects.first()
        officers_head = OfficersHead.objects.first()
        officers_spokes_person = OfficersSpokesPerson.objects.all()
        information_officer = InformationOfficer.objects.all()
        national_council_head_serializer = NationalCouncilHeadSerializer(
            national_council_head)
        executive_committe_head_serializer = ExecutiveCommitteHeadSerializer(
            executive_committe_head)
        officers_head_serializer = OfficersHeadSerializer(officers_head)
        officers_spokes_person_serializer = OfficersSpokesPersonSerializer(
            officers_spokes_person, many=True)
        information_officer_serializer = InformationOfficerSerializer(
            information_officer, many=True)

        results = [
            {
                "id": 1,
                "national_council_head": national_council_head_serializer.data,
                "executive_committe_head": executive_committe_head_serializer.data,
                "officers_head": officers_head_serializer.data,
                "officers_spokesperson": officers_spokes_person_serializer.data,
                "information_officer": information_officer_serializer.data,
            }
        ]

        return Response({"results": results})
