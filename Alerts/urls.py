from django.urls import path
from .views import AlertListView, AlertInstanceView

urlpatterns = [
    path('alerts/', AlertListView.as_view(), name='alert-list'),
    path('alerts/<int:pk>/', AlertInstanceView.as_view(), name='alert-instance'),
]
