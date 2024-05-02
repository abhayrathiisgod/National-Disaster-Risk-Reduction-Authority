from django.contrib import admin
from bulletin.models import Bulletin, BulletinAuthor, BulletinType


class BulletinAuthorAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'author', 'author_ne')
    list_display_links = ('id', 'author', 'author_ne')
    readonly_fields = ('author', 'author_ne')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False


class BulletinAdmin(admin.ModelAdmin):
    actions = None

    list_display = ('bulletin_author', 'bulletin_type', 'title', 'date')
    list_display_links = ('bulletin_author', 'bulletin_type', 'title', 'date')
    list_filter = ('date', 'bulletin_author', 'bulletin_type')
    search_fields = ('title',)

    def has_change_permission(self, request, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False


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
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Bulletin, BulletinAdmin)
admin.site.register(BulletinAuthor, BulletinAuthorAdmin)
admin.site.register(BulletinType, BulletinTypeAdmin)
