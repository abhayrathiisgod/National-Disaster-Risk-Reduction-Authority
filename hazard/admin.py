from django.contrib import admin
from .models import Hazards
# Register your models here.


class HazardsAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'title', 'order', 'type')
    list_display_links = ('id', 'title', 'order', 'type')
    list_filter = ('type',)
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


admin.site.register(Hazards, HazardsAdmin)
