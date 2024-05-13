from django.contrib import admin
from django.http import HttpRequest
from .models import PublicationAuthor, Publications, PublicationType


class PublicationTypeAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'publication_type', 'publication_type_ne')
    list_display_links = ('id', 'publication_type', 'publication_type_ne')
    list_filter = ('publication_type',)
    search_fields = ('publication_type', 'title')

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False


class PublicationAuthorAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'publication_author', 'publication_author_ne')
    list_display_links = ('id', 'publication_author', 'publication_author_ne')
    search_fields = ('publication_author',)

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False


class PublicationsAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'pub_type', 'title', 'date', 'is_published')
    list_display_links = ('id', 'title', 'date', 'is_published')
    list_filter = ('pub_type', 'id', 'date', 'is_published')
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


admin.site.register(PublicationType, PublicationTypeAdmin)
admin.site.register(PublicationAuthor, PublicationAuthorAdmin)
admin.site.register(Publications, PublicationsAdmin)
