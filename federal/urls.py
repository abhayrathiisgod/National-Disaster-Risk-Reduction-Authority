from django.urls import path
from federal.views import ProvinceView, DistrictView, MunicipalityView, WardView

urlpatterns = [
    path('provinces/', ProvinceView.as_view()),
    path('districts/', DistrictView.as_view()),
    path('municipalities/', MunicipalityView.as_view()),
    path('wards/', WardView.as_view()),
]
