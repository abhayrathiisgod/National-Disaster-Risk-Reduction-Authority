from django.contrib import admin
from galleries.models import Gallery, GalleryImage, VideoGallery
from django.contrib.admin.options import TabularInline
from django.db import models


class GalleryImageInline(TabularInline):
    extra = 1
    model = GalleryImage


class GalleryAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    readonly_fields = ('image_preview',)
    inlines = (GalleryImageInline,)

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
    readonly_fields = ('image_preview',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(GalleryImageAdmin, self).get_form(request, obj, **kwargs)

        gallery_field = form.base_fields.get("gallery")
        if gallery_field:
            gallery_field.widget.can_add_related = False
            gallery_field.widget.can_change_related = False
            gallery_field.widget.can_delete_related = False
            gallery_field.widget.can_view_related = False

        return form

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
