from django.urls import path
from pressnotenews.views import NewsInfoViewsetList, PressNoteAPIView, NewsInfoViewsetInstance, PressNoteListAPIView

urlpatterns = [
    path('newsinfo/', NewsInfoViewsetList.as_view()),
    path('newsinfo/<int:pk>/',
         NewsInfoViewsetInstance.as_view()),
    path('press-note/', PressNoteListAPIView.as_view()),
    path('press-note/<int:pk>', PressNoteAPIView.as_view()),
]
