from django.urls import path
from . import views
from .views import PageView, NdrmaViewSet, HomePageBannerViewSet, ContactListView, FrequentlyAskedQuestionsView, WardDocumentView, ContactDetailView, IntroductionView, BookmarksView, MenuViewSet
urlpatterns = [
    path('pages/national-platform-of-disaster-risk-re/', PageView.as_view()),
    path('faq/', FrequentlyAskedQuestionsView.as_view({'get': 'list'})),
    path('faq/<int:pk>/',
         FrequentlyAskedQuestionsView.as_view({'get': 'retrieve'})),
    path('ward-document/', WardDocumentView.as_view({'get': 'list'})),
    path('ward-document/<int:pk>/',
         WardDocumentView.as_view({'get': 'retrieve'})),
    path('contact-details/', ContactDetailView.as_view()),
    path('introduction/', IntroductionView.as_view({'get': 'list'})),
    path('introduction/<int:pk>/',
         IntroductionView.as_view({'get': 'retrieve'})),
    path('bookmarks/', BookmarksView.as_view({'get': 'list'})),
    path('bookmarks/<int:pk>/', BookmarksView.as_view({'get': 'retrieve'})),
    path('menu/', MenuViewSet.as_view({'get': 'list'})),
    path('menu/<int:pk>/', MenuViewSet.as_view({'get': 'retrieve'})),
    path('contacts/', ContactListView.as_view(), name='contact-list'),
    path('homepagebanner/',
         HomePageBannerViewSet.as_view({'get': 'list'})),
    path('homepagebanner/<int:pk>/',
         HomePageBannerViewSet.as_view({'get': 'retrieve'})),
    path('ndrmaportals/',
         NdrmaViewSet.as_view({'get': 'list'})),
    path('ndrmaportals/<int:pk>/',
         NdrmaViewSet.as_view({'get': 'retrieve'})),
]
