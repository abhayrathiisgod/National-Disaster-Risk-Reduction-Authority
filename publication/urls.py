from django.urls import path
from .views import PublicationViewSet

urlpatterns = [
    path('', PublicationViewSet.as_view({'get': 'list'}),
         name='publication_detail'),
    path('<slug:slug>/', PublicationViewSet.as_view(
        {'get': 'retrieve'}), name='all_publications'),
]
