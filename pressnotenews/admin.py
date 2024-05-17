from django.contrib import admin
from django.http import HttpRequest
from pressnotenews.models import NewsInfo, Author, Type, PressNote


class AuthorAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('Author_id', 'name')
    list_display_links = ('Author_id', 'name')
    search_fields = ('name', 'name_ne')

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


class TypeAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('Type_id', 'name')
    list_display_links = ('Type_id', 'name')
    search_fields = ('name', 'name_ne')

    def has_add_permission(self, request):
        if Type.objects.count() <= 7:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class NewsInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
    list_display_links = ('id', 'title', 'date')
    search_fields = ('title', 'description', 'summary')
    list_filter = ('id', 'date',)
    readonly_fields = ('slug',)

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


class PressNoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'type', 'title', 'date', 'is_published')
    list_display_links = ('id', 'author', 'type',
                          'title', 'date', 'is_published')
    search_fields = ('title', 'description', 'summary')
    list_filter = ('author', 'type', 'date', 'is_published')
    readonly_fields = ('slug', 'image')

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


admin.site.register(Author, AuthorAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(NewsInfo, NewsInfoAdmin)
admin.site.register(PressNote, PressNoteAdmin)
