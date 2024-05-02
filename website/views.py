from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Page, Introduction, ContactForm, ContactDetail, WardDocument, FrequentlyAskedQuestions, Bookmarks, Menu, HomePageBanner
from .serializers import PageSerializer, ContactSerializer, IntroductionSerializer, ContactDetailSerializer, WardDocumentSerializer, FrequentlyAskedQuestionsSerializer, HomePageBannerSerializer, BookmarksSerializer, MenuSerializer
from rest_framework.response import Response
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


class ContactListView(generics.ListCreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactSerializer


class BookmarksView(generics.ListAPIView):
    queryset = Bookmarks.objects.all()
    serializer_class = BookmarksSerializer
    pagination_class = None


class BookmarksDetailView(generics.RetrieveAPIView):
    queryset = Bookmarks.objects.all()
    serializer_class = BookmarksSerializer
    pagination_class = None
    lookup_field = 'pk'


class MenuViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Menu.objects.filter(children__isnull=False).distinct()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = MenuSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        menuuu = get_object_or_404(queryset, id=pk)
        serializer = MenuSerializer(menuuu)
        return Response(serializer.data)


class HomePageListView(generics.ListAPIView):
    queryset = HomePageBanner.objects.all()
    serializer_class = HomePageBannerSerializer


class HomePageView(generics.RetrieveAPIView):
    queryset = HomePageBanner.objects.all()
    serializer_class = HomePageBannerSerializer
    lookup_field = 'pk'
