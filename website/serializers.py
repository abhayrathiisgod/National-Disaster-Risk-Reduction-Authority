from rest_framework import serializers, viewsets
from .models import HomePageBanner, ContactDetail, NdrmaPortals, Introduction, WardDocument, ContactForm, FrequentlyAskedQuestions, Page, Bookmarks, Menu


class ContactDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetail
        fields = '__all__'


class IntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction
        fields = '__all__'


class WardDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardDocument
        fields = '__all__'


class FrequentlyAskedQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentlyAskedQuestions
        fields = '__all__'


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'


class BookmarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmarks
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ['id', 'name', 'name_ne', 'parent', 'link',
                  'is_external_link', 'content_source', 'page', 'children']

    def get_children(self, obj):
        children = Menu.objects.filter(parent=obj)
        serializer = MenuSerializer(children, many=True)
        return serializer.data


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'


class HomePageBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePageBanner
        fields = '__all__'


class NdrmaportalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NdrmaPortals
        fields = '__all__'
