from django.contrib import admin
from django.http import HttpRequest
from bulletin.models import Bulletin, BulletinAuthor, BulletinType


class BulletinAuthorAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'author', 'author_ne')
    list_display_links = ('id', 'author', 'author_ne')
    readonly_fields = ('author', 'author_ne')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False


class BulletinAdmin(admin.ModelAdmin):

    list_display = ('bulletin_author', 'bulletin_type', 'title', 'date')
    list_display_links = ('bulletin_author', 'bulletin_type', 'title', 'date')
    list_filter = ('date', 'bulletin_author', 'bulletin_type')
    search_fields = ('title',)
    readonly_fields = ('slug',)

    def has_change_permission(self, request, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False

    def get_form(self, request, obj=None, **kwargs):
        form = super(BulletinAdmin, self).get_form(request, obj, **kwargs)

        bulletin_author_field = form.base_fields.get("bulletin_author")
        if bulletin_author_field:
            bulletin_author_field.widget.can_add_related = False
            bulletin_author_field.widget.can_change_related = False
            bulletin_author_field.widget.can_delete_related = False
            bulletin_author_field.widget.can_view_related = False

        bulletin_type_field = form.base_fields.get("bulletin_type")
        if bulletin_type_field:
            bulletin_type_field.widget.can_add_related = False
            bulletin_type_field.widget.can_change_related = False
            bulletin_type_field.widget.can_delete_related = False
            bulletin_type_field.widget.can_view_related = False
        return form


class BulletinTypeAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'bulletin_type')
    list_display_links = ('id', 'bulletin_type')
    list_filter = ('id', 'bulletin_type')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False


admin.site.register(Bulletin, BulletinAdmin)
admin.site.register(BulletinAuthor, BulletinAuthorAdmin)
admin.site.register(BulletinType, BulletinTypeAdmin)
