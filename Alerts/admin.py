from django.contrib import admin
from .models import AlertList
# Register your models here.


class AlertListAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'title', 'source', 'verified', 'public',
                    'region', 'regionId', 'hazard')
    list_filter = ('id', 'title', 'source', 'verified', 'public',
                   'region', 'regionId', 'hazard')
    list_display_links = ('id', 'title', 'source', 'verified', 'public',
                          'region', 'regionId', 'hazard')
    readonly_fields = ('createdBy', 'expireOn')

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


admin.site.register(AlertList, AlertListAdmin)
