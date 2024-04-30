from django.contrib import admin
from .models import Guidechildren, GuideCourse, Course


class GuideCourseAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'name', 'title')
    list_display_links = ('id', 'name', 'title')
    search_fields = ('name', 'title')

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


class GuidechildrenAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'name', 'title')
    list_display_links = ('id', 'name', 'title')
    search_fields = ('name', 'title')

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


class CourseAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'title', 'skill_level', 'language')
    list_display_links = ('id', 'title', 'skill_level', 'language')
    list_filter = ('skill_level', 'language')
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


admin.site.register(GuideCourse, GuideCourseAdmin)
admin.site.register(Guidechildren, GuidechildrenAdmin)
admin.site.register(Course, CourseAdmin)
