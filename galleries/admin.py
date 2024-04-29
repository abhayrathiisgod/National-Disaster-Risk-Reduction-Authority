from django.contrib import admin
from galleries.models import Gallery, GalleryImage, VideoGallery

# Register your models here.
admin.site.register(Gallery)
admin.site.register(GalleryImage)
admin.site.register(VideoGallery)
