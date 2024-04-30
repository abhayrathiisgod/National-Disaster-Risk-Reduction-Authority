from django.contrib import admin
from django.http import HttpRequest
from website.models import Page, ContactDetail, Introduction, WardDocument, ContactForm, FrequentlyAskedQuestions, Bookmarks, Menu


class ContactDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'detail', 'detail_ne')
    list_display_links = ('id', 'detail', 'detail_ne')
    search_fields = ('detail',)

    def has_delete_permission(self, request, obj=None):

        return False

    def has_add_permission(self, request, obj=None):

        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False


class IntroductionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sub_title')
    list_display_links = ('id', 'title', 'sub_title')
    search_fields = ('title', 'sub_title')

    def has_delete_permission(self, request, obj=None):

        return False

    def has_add_permission(self, request, obj=None):

        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False


class WardDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'filename')
    list_display_links = ('id', 'filename')
    search_fields = ('filename',)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False


class FrequentlyAskedQuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')
    list_display_links = ('id', 'question')
    search_fields = ('question',)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False


class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    list_filter = ('id',)
    search_fields = ('title',)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False


class BookmarksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')
    list_display_links = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('anme',)

    def has_delete_permission(self, request, obj=None):

        return False

    def has_add_permission(self, request, obj=None):

        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'link',
                    'is_external_link', 'content_source', 'page')
    list_display_links = ('id', 'name', 'parent', 'link',
                          'is_external_link', 'content_source', 'page')
    list_filter = ('id', 'is_external_link')

    search_fields = ('name',)

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'phone', 'subject')
    list_display_links = ('id', 'full_name', 'email', 'phone', 'subject')

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):

        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        if request.user.is_superuser:
            return True
        return False


admin.site.register(ContactDetail, ContactDetailAdmin)
admin.site.register(Introduction, IntroductionAdmin)
admin.site.register(WardDocument, WardDocumentAdmin)
admin.site.register(FrequentlyAskedQuestions, FrequentlyAskedQuestionsAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Bookmarks, BookmarksAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
