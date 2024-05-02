from django.shortcuts import render
from rest_framework import generics
from .models import Publications
from .serializers import PublicationsSerializer, PublicationsDetailSerializer
from rest_framework.pagination import LimitOffsetPagination
# Create your views here.


class Allpublicationview(generics.ListAPIView):
    queryset = Publications.objects.all()
    serializer_class = PublicationsSerializer
    pagination_class = LimitOffsetPagination


class DecisionCircularDirectivePublicationListView(generics.ListAPIView):
    queryset = Publications.objects.filter(
        pub_type__publication_type='Decision/Circular/Directive')
    serializer_class = PublicationsSerializer
    pagination_class = LimitOffsetPagination


class RulesAndRegulationsPublicationListView(generics.ListAPIView):
    queryset = Publications.objects.filter(
        pub_type__publication_type='Rules and Regulations')
    serializer_class = PublicationsSerializer
    pagination_class = LimitOffsetPagination


class PoliciesAndDirectoriesPublicationListView(generics.ListAPIView):
    queryset = Publications.objects.filter(
        pub_type__publication_type='Policies and Directories')
    serializer_class = PublicationsSerializer
    pagination_class = LimitOffsetPagination


class ReportPublicationListView(generics.ListAPIView):
    queryset = Publications.objects.filter(pub_type__publication_type='Report')
    serializer_class = PublicationsSerializer
    pagination_class = LimitOffsetPagination


class ProcedurePublicationListView(generics.ListAPIView):
    queryset = Publications.objects.filter(
        pub_type__publication_type='Procedure')
    serializer_class = PublicationsSerializer
    pagination_class = LimitOffsetPagination


class PlanPublicationListView(generics.ListAPIView):
    queryset = Publications.objects.filter(pub_type__publication_type='Plan')
    serializer_class = PublicationsSerializer
    pagination_class = LimitOffsetPagination


class ArticlesPublicationListView(generics.ListAPIView):
    queryset = Publications.objects.filter(
        pub_type__publication_type='Articles')
    serializer_class = PublicationsSerializer
    pagination_class = LimitOffsetPagination


class CriteriaPublicationListView(generics.ListAPIView):
    queryset = Publications.objects.filter(
        pub_type__publication_type='Criteria')
    serializer_class = PublicationsSerializer
    pagination_class = LimitOffsetPagination


class MeetingReportPublicationListView(generics.ListAPIView):
    queryset = Publications.objects.filter(
        pub_type__publication_type='MeetingReport')
    serializer_class = PublicationsSerializer
    pagination_class = LimitOffsetPagination


class TenderPublicationListView(generics.ListAPIView):
    queryset = Publications.objects.filter(pub_type__publication_type='Tender')
    serializer_class = PublicationsSerializer
    pagination_class = LimitOffsetPagination


class PublicationDetailView(generics.RetrieveAPIView):
    queryset = Publications.objects.all()
    serializer_class = PublicationsDetailSerializer
    lookup_field = 'pk'
