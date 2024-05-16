from django.urls import path
from .views import GalleryView, VideoGalleryView

urlpatterns = [
    path('photo-gallery/', GalleryView.as_view({'get': 'list'})),
    path('photo-gallery/<int:pk>/', GalleryView.as_view({'get': 'retrieve'})),
    path('video-gallery/', VideoGalleryView.as_view({'get': 'list'})),
    path('video-gallery/<int:pk>/',
         VideoGalleryView.as_view({'get': 'retrieve'})),
]
