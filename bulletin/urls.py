from django.urls import path
from .views import BulletinList, BulletinNationalList, BulletinDateWiseList


urlpatterns = [
    path('bulletinss/', BulletinList.as_view()),
    path('bulletinss/national/', BulletinNationalList.as_view()),
    path('bulletinss/datewise/', BulletinDateWiseList.as_view()),
]
