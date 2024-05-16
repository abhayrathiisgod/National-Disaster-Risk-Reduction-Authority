from django.urls import path
from .views import AlertView

urlpatterns = [
    path('alerts/', AlertView.as_view({'get': 'list'}), name='alert-list'),
    path('alerts/<int:pk>/',
         AlertView.as_view({'get': 'retrieve'}), name='alert-instance'),
]
