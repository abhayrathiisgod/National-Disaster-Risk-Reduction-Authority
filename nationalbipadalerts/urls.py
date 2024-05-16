from django.urls import path
from .views import BipadAlertsView

urlpatterns = [
    path('nationalbipadalerts/', BipadAlertsView.as_view({'get': 'list'}),
         name='nationalbipadalerts'),
    path('nationalbipadalerts/<int:pk>/', BipadAlertsView.as_view({'get': 'retrieve'}),
         name='nationalbipadalerts_detail'),

]
