from django.contrib import admin
from .models import Address, Donater, Project, Training
from django_filters.rest_framework import DjangoFilterBackend


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'local_address', 'local_address_ne')
    list_display_links = ('id', 'local_address', 'local_address_ne')
    search_fields = ('loacl_address',)

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


class DonaterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link',
                    'donater_created_at', 'donater_updated_at')
    list_display_links = ('id', 'name', 'link',
                          'donater_created_at', 'donater_updated_at')
    list_filter = ('donater_created_at', 'donater_updated_at')
    search_fields = ('name',)

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


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'budget', 'start_date',
                    'end_date', 'created_at', 'updated_at', 'deleted_at')
    list_display_links = ('id', 'title', 'budget', 'start_date',
                          'end_date', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('start_date', 'end_date', 'created_at',
                   'updated_at', 'deleted_at')
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


class TrainingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'startDate', 'endDate',
                    'num_of_participants', 'province', 'district', 'municipality')
    list_display_links = ('id', 'title')
    list_filter = ('startDate', 'endDate', 'province', 'district')
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


admin.site.register(Address, AddressAdmin)
admin.site.register(Donater, DonaterAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Training, TrainingAdmin)
