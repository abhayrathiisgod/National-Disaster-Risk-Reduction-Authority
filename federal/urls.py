from django.urls import path
from federal.views import ProvinceView, ProvinceInstanceView, DistrictInstanceView, MunicipalityInstanceView, WardInstanceView, DistrictView, MunicipalityView, WardView

urlpatterns = [
    path('provinces/', ProvinceView.as_view()),
    path('provinces/<int:pk>/', ProvinceInstanceView.as_view()),
    path('districts/', DistrictView.as_view()),
    path('districts/<int:pk>/', DistrictInstanceView.as_view()),
    path('municipalities/', MunicipalityView.as_view()),
    path('municipalities/<int:pk>/', MunicipalityInstanceView.as_view()),
    path('wards/', WardView.as_view()),
    path('wards/<int:pk>/', WardInstanceView.as_view()),
]
