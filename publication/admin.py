from django.contrib import admin
from django.http import HttpRequest
from .models import PublicationAuthor, Publications, PublicationType


class PublicationTypeAdmin(admin.ModelAdmin):

    actions = None
    list_display = ('id', 'publication_type', 'publication_type_ne')
    list_display_links = ('id', 'publication_type', 'publication_type_ne')

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None) -> bool:
        return False


class PublicationAuthorAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'publication_author', 'publication_author_ne')
    list_display_links = ('id', 'publication_author', 'publication_author_ne')

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False


class PublicationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'pub_type', 'title', 'date', 'is_published')
    list_display_links = ('id', 'title', 'date', 'is_published')
    list_filter = ('pub_type', 'date', 'is_published')
    readonly_fields = ('slug', 'image')
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

    def get_form(self, request, obj=None, **kwargs):

        form = super(PublicationsAdmin, self).get_form(request, obj, **kwargs)

        pub_type_field = form.base_fields.get("pub_type")

        if pub_type_field:
            pub_type_field.widget.can_add_related = False
            pub_type_field.widget.can_change_related = False
            pub_type_field.widget.can_delete_related = False

        pub_author_field = form.base_fields.get("pub_author")

        if pub_author_field:
            pub_author_field.widget.can_add_related = False
            pub_author_field.widget.can_change_related = False
            pub_author_field.widget.can_delete_related = False

        return form


admin.site.register(PublicationType, PublicationTypeAdmin)
admin.site.register(PublicationAuthor, PublicationAuthorAdmin)
admin.site.register(Publications, PublicationsAdmin)
