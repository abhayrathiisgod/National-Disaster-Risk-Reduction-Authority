from django.urls import path
from .views import BulletinViewSets


urlpatterns = [
    path('bulletins/', BulletinViewSets.as_view({'get': 'list'})),
    path('bulletin/<slug:slug>/',
         BulletinViewSets.as_view({'get': 'retrieve'})),
]
