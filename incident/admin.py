from django.contrib import admin
from .models import Loss, Incident


class LossAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'createdOn', 'modifiedOn', 'estimatedLoss')
    list_display_links = ('id', 'createdOn', 'modifiedOn', 'estimatedLoss')
    search_fields = ('id', 'description')
    list_filter = ('createdOn', 'modifiedOn')

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


class IncidentAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'title', 'createdOn',
                    'modifiedOn', 'verified', 'approved')
    list_display_links = ('id', 'title', 'createdOn',
                          'modifiedOn', 'verified', 'approved')
    search_fields = ('title', 'description', 'streetAddress')
    list_filter = ('createdOn', 'modifiedOn', 'verified', 'approved', 'hazard')

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


admin.site.register(Loss, LossAdmin)
admin.site.register(Incident, IncidentAdmin)
