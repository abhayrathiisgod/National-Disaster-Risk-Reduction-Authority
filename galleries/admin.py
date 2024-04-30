from django.contrib import admin
from galleries.models import Gallery, GalleryImage, VideoGallery


class GalleryAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False


class GalleryImageAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'gallery', 'title', 'photo_credit')
    list_display_links = ('id', 'gallery', 'title', 'photo_credit')
    list_filter = ('id', 'gallery__title')
    search_fields = ('title', 'photo_credit')

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False


class VideoGalleryAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'youtube_url')
    list_display_links = ('id', 'youtube_url')
    search_fields = ('youtube_url',)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False


# Register the admin classes
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(VideoGallery, VideoGalleryAdmin)
