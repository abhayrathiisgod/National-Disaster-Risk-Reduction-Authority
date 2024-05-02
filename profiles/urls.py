from django.urls import path
from . import views

urlpatterns = [
    path('skills/', views.SkillsListAPIView.as_view(), name='skills-list'),
    path('skills/<int:pk>/', views.SkillsAPIView.as_view(), name='skills-detail'),

    path('designation/', views.DesignationListAPIView.as_view(),
         name='designation-list'),
    path('designation/<int:pk>/', views.DesignationAPIView.as_view(),
         name='designation-detail'),

    path('department/', views.DepartmentListAPIView.as_view(),
         name='department-list'),
    path('department/<int:pk>/', views.DepartmentAPIView.as_view(),
         name='department-detail'),

    path('trainingorg/', views.TrainingOrgListAPIView.as_view(),
         name='trainingorg-list'),
    path('trainingorg/<int:pk>/', views.TrainingOrgAPIView.as_view(),
         name='trainingorg-detail'),

    path('trainingcertificate/', views.TrainingCertificateListAPIView.as_view(),
         name='trainingcertificate-list'),
    path('trainingcertificate/<int:pk>/',
         views.TrainingCertificateAPIView.as_view(), name='trainingcertificate-detail'),

    path('trainings/', views.TrainingsListAPIView.as_view(), name='trainings-list'),
    path('trainings/<int:pk>/', views.TrainingsAPIView.as_view(),
         name='trainings-detail'),

    path('officerprofile/', views.OfficerProfileListAPIView.as_view(),
         name='officerprofile-list'),
    path('officerprofile/<int:pk>/', views.OfficerProfileAPIView.as_view(),
         name='officerprofile-detail'),

    path('commiteprofile/', views.CommiteProfileListAPIView.as_view(),
         name='commiteprofile-list'),
    path('commiteprofile/<int:pk>/',

         views.CommiteProfileInstanceView.as_view(), name='commiteprofile-detail'),
    path('nationalcouncilhead/', views.NationalCouncilHeadListAPIView.as_view(),
         name='nationalcouncilhead-list'),
    path('nationalcouncilhead/<int:pk>/',
         views.NationalCouncilHeadAPIView.as_view(), name='nationalcouncilhead-detail'),

    path('executivecommittehead/', views.ExecutiveCommitteHeadListAPIView.as_view(),
         name='executivecommittehead-list'),
    path('executivecommittehead/<int:pk>/',
         views.ExecutiveCommitteHeadAPIView.as_view(), name='executivecommittehead-detail'),

    path('officershead/', views.OfficersHeadListAPIView.as_view(),
         name='officershead-list'),
    path('officershead/<int:pk>/', views.OfficersHeadAPIView.as_view(),
         name='officershead-detail'),

    path('officersspokesperson/', views.OfficersSpokesPersonListAPIView.as_view(),
         name='officersspokesperson-list'),
    path('officersspokesperson/<int:pk>/',
         views.OfficersSpokesPersonAPIView.as_view(), name='officersspokesperson-detail'),

    path('informationofficer/', views.InformationOfficerListAPIView.as_view(),
         name='informationofficer-list'),
    path('informationofficer/<int:pk>/',
         views.InformationOfficerAPIView.as_view(), name='informationofficer-detail'),

    path('officerprofileview/', views.OfficerProfileView.as_view(),
         name='officerprofileview'),
    path('officerprofileview/<int:pk>/',
         views.OfficerProfileInstanceView.as_view(), name='officerprofileview-detail'),

    path('councilprofileview/', views.CouncilProfileView.as_view(),
         name='councilprofileview'),
]
