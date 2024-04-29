from django.urls import path
from .views import PageView, FrequentlyAskedQuestionsView, FrequentlyAskedQuestionsDetailView, WardDocumentView, WardDocumentDetailView, ContactDetailView, IntroductionView, IntroductionDetailView
urlpatterns = [
    path('pages/national-platform-of-disaster-risk-re/', PageView.as_view()),
    path('faq/', FrequentlyAskedQuestionsView.as_view()),
    path('faq/<int:pk>/', FrequentlyAskedQuestionsDetailView.as_view()),
    path('ward-document/', WardDocumentView.as_view()),
    path('ward-document/<int:pk>/', WardDocumentDetailView.as_view()),
    path('contact-details/', ContactDetailView.as_view()),
    path('introduction/', IntroductionView.as_view()),
    path('introduction/<int:pk>/', IntroductionDetailView.as_view()),
]
