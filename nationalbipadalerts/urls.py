from django.urls import path
from .views import ImportantLinksList, BipadAlertsList, BipadAlertView

urlpatterns = [
    path('nationalbipadalerts/', BipadAlertsList.as_view(),
         name='nationalbipadalerts'),
    path('nationalbipadalerts/<int:pk>', BipadAlertView.as_view(),
         name='nationalbipadalerts_detail'),

]
