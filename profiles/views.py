from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .models import Skills, Designation, Department, TrainingOrg, TrainingCertificate, Trainings, OfficerProfile, CommiteProfile, NationalCouncilHead, ExecutiveCommitteHead, OfficersHead, OfficersSpokesPerson, InformationOfficer
from profiles.serializers import SkillsSerializer, OfficerProfileListSerializer, DesignationSerializer, DepartmentSerializer, TrainingOrgSerializer, TrainingCertificateSerializer, TrainingsSerializer, OfficerProfileSerializer, CommiteProfileSerializer, NationalCouncilHeadSerializer, ExecutiveCommitteHeadSerializer, OfficersHeadSerializer, OfficersSpokesPersonSerializer, InformationOfficerSerializer
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, get_object_or_404


class SkillsAPIView(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    pagination_class = LimitOffsetPagination
    lookup_field = 'pk'


class DesignationAPIView(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    pagination_class = LimitOffsetPagination
    lookup_field = 'pk'


class DepartmentAPIView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    pagination_class = LimitOffsetPagination
    lookup_field = 'pk'


class TrainingOrgAPIView(viewsets.ModelViewSet):
    queryset = TrainingOrg.objects.all()
    serializer_class = TrainingOrgSerializer
    pagination_class = LimitOffsetPagination
    lookup_field = 'pk'


class TrainingCertificateAPIView(viewsets.ModelViewSet):
    queryset = TrainingCertificate.objects.all()
    serializer_class = TrainingCertificateSerializer
    pagination_class = LimitOffsetPagination
    lookup_field = 'pk'


class TrainingsAPIView(viewsets.ModelViewSet):
    queryset = Trainings.objects.all()
    serializer_class = TrainingsSerializer
    pagination_class = LimitOffsetPagination
    lookup_field = 'pk'


class OfficerProfileAPIView(viewsets.ModelViewSet):
    queryset = OfficerProfile.objects.all().order_by('order')
    pagination_class = LimitOffsetPagination
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.action == 'list':
            return OfficerProfileListSerializer
        elif self.action == 'retrieve':
            return OfficerProfileSerializer
        return OfficerProfileSerializer


class CommiteProfileAPIView(viewsets.ModelViewSet):
    queryset = CommiteProfile.objects.all().order_by('order')
    serializer_class = CommiteProfileSerializer
    pagination_class = LimitOffsetPagination
    lookup_field = 'pk'


class NationalCouncilHeadAPIView(viewsets.ModelViewSet):
    queryset = NationalCouncilHead.objects.all().order_by('order')
    serializer_class = NationalCouncilHeadSerializer
    pagination_class = LimitOffsetPagination
    lookup_field = 'pk'


class ExecutiveCommitteHeadAPIView(viewsets.ModelViewSet):
    queryset = ExecutiveCommitteHead.objects.all().order_by('order')
    serializer_class = ExecutiveCommitteHeadSerializer
    pagination_class = LimitOffsetPagination
    lookup_field = 'pk'


class OfficersHeadAPIView(viewsets.ModelViewSet):
    queryset = OfficersHead.objects.all().order_by('order')
    serializer_class = OfficersHeadSerializer
    pagination_class = LimitOffsetPagination
    lookup_field = 'pk'


class OfficersSpokesPersonAPIView(viewsets.ModelViewSet):
    queryset = OfficersSpokesPerson.objects.all().order_by('order')
    serializer_class = OfficersSpokesPersonSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['designation']
    lookup_field = 'pk'


class InformationOfficerAPIView(viewsets.ModelViewSet):
    queryset = InformationOfficer.objects.all().order_by('order')
    serializer_class = InformationOfficerSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['designation']
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
