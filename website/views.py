from django.shortcuts import render
from rest_framework import generics
from .models import Page, Introduction, ContactDetail, WardDocument, FrequentlyAskedQuestions
from .serializers import PageSerializer, IntroductionSerializer, ContactDetailSerializer, WardDocumentSerializer, FrequentlyAskedQuestionsSerializer

# Create your views here.


class IntroductionView(generics.ListAPIView):
    queryset = Introduction.objects.all()
    serializer_class = IntroductionSerializer
    pagination_class = None


class IntroductionDetailView(generics.RetrieveAPIView):
    queryset = Introduction.objects.all()
    serializer_class = IntroductionSerializer
    pagination_class = None
    lookup_field = 'pk'


class ContactDetailView(generics.ListAPIView):
    queryset = ContactDetail.objects.all()
    serializer_class = ContactDetailSerializer
    pagination_class = None


class WardDocumentView(generics.ListAPIView):
    queryset = WardDocument.objects.all()
    serializer_class = WardDocumentSerializer
    pagination_class = None


class WardDocumentDetailView(generics.RetrieveAPIView):
    queryset = WardDocument.objects.all()
    serializer_class = WardDocumentSerializer
    pagination_class = None
    lookup_field = 'pk'


class FrequentlyAskedQuestionsView(generics.ListAPIView):
    queryset = FrequentlyAskedQuestions.objects.all()
    serializer_class = FrequentlyAskedQuestionsSerializer
    pagination_class = None


class FrequentlyAskedQuestionsDetailView(generics.RetrieveAPIView):
    queryset = FrequentlyAskedQuestions.objects.all()
    serializer_class = FrequentlyAskedQuestionsSerializer
    pagination_class = None
    lookup_field = 'pk'


class PageView(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    pagination_class = None
