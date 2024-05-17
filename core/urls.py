from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/importantcontacts/', include('importantcontacts.urls')),
    path('api/v1/bulletin/', include('bulletin.urls')),
    path('api/v1/federal/', include('federal.urls')),
    path('api/v1/pressnotenews/', include('pressnotenews.urls')),
    path('api/v1/guidecourse/', include('guidecourse.urls')),
    path('api/v1/galleries/', include('galleries.urls')),
    path('api/v1/trainingprojects/', include('trainingprojects.urls')),
    path('api/v1/website/', include('website.urls')),
    path('api/v1/publications/', include('publication.urls')),
    path('api/v1/alerts/', include('Alerts.urls')),
    path('api/v1/hazards/', include('hazard.urls')),
    path('api/v1/incidents/', include('incident.urls')),
    path('api/v1/officerprofileinfos/', include('profiles.urls')),
    path('api/v1/nationalbipadalerts/', include('nationalbipadalerts.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
