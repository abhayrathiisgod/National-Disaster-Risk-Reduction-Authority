from django.urls import path
from .views import GalleryView, GalleryDetailView, VideoGalleryView, VideoGalleryDetailView

urlpatterns = [
    path('photo-gallery/', GalleryView.as_view()),
    path('photo-gallery/<int:pk>/', GalleryDetailView.as_view()),
    path('video-gallery/', VideoGalleryView.as_view()),
    path('video-gallery/<int:pk>/', VideoGalleryDetailView.as_view()),

]
