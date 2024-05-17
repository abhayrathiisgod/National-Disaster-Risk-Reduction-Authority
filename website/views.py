from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Page, Introduction, NdrmaPortals, ContactForm, ContactDetail, WardDocument, FrequentlyAskedQuestions, Bookmarks, Menu, HomePageBanner
from .serializers import PageSerializer, NdrmaportalSerializer, ContactSerializer, IntroductionSerializer, ContactDetailSerializer, WardDocumentSerializer, FrequentlyAskedQuestionsSerializer, HomePageBannerSerializer, BookmarksSerializer, MenuSerializer
from rest_framework.response import Response
from rest_framework import filters
# Create your views here.


class IntroductionView(viewsets.ModelViewSet):
    queryset = Introduction.objects.all()
    serializer_class = IntroductionSerializer
    lookup_field = 'pk'


class ContactDetailView(generics.ListAPIView):
    queryset = ContactDetail.objects.all()
    serializer_class = ContactDetailSerializer
    pagination_class = None


class WardDocumentView(viewsets.ModelViewSet):
    queryset = WardDocument.objects.all()
    serializer_class = WardDocumentSerializer
    lookup_field = 'pk'


class FrequentlyAskedQuestionsView(viewsets.ModelViewSet):
    queryset = FrequentlyAskedQuestions.objects.all()
    serializer_class = FrequentlyAskedQuestionsSerializer
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['question']


class PageView(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    pagination_class = None
    lookup_field = 'slug'


class ContactListView(generics.ListCreateAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactSerializer


class BookmarksView(viewsets.ModelViewSet):
    queryset = Bookmarks.objects.all()
    serializer_class = BookmarksSerializer
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


class HomePageBannerViewSet(viewsets.ModelViewSet):
    queryset = HomePageBanner.objects.all()
    serializer_class = HomePageBannerSerializer
    lookup_field = 'pk'


class NdrmaViewSet(viewsets.ModelViewSet):
    queryset = NdrmaPortals.objects.all()
    serializer_class = NdrmaportalSerializer
    lookup_field = 'pk'
