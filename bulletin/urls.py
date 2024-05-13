from django.urls import path
from .views import BulletinList, BulletinNationalList, BulletinDateWiseList, BulletindailylList


urlpatterns = [
    path('bulletinss/', BulletinList.as_view()),
    path('national/', BulletinNationalList.as_view()),
    path('daily/', BulletindailylList.as_view()),
    path('bulletinss/datewise/', BulletinDateWiseList.as_view()),
]
