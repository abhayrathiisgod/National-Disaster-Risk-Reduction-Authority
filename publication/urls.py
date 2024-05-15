from django.urls import path
from .views import PublicationDetailView, Allpublicationview

urlpatterns = [
    path('<int:pk>/', PublicationDetailView.as_view(), name='publication_detail'),
    path('', Allpublicationview.as_view(), name='all_publications'),
]
