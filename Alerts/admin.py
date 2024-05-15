from django.contrib import admin
from .models import AlertList
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
# Register your models here.

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(Site)


class AlertListAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'title', 'source', 'verified', 'public',
                    'region', 'regionId', 'hazard')
    list_filter = ('verified', 'public', 'hazard')
    list_display_links = ('id', 'title', 'source', 'verified', 'public',
                          'region', 'regionId', 'hazard')
    readonly_fields = ('createdBy', 'expireOn', 'updatedBy')

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
        form = super(AlertListAdmin, self).get_form(request, obj, **kwargs)

        wards_field = form.base_fields.get("wards")
        if wards_field:
            wards_field.widget.can_add_related = False
            wards_field.widget.can_change_related = False
            wards_field.widget.can_delete_related = False
            wards_field.widget.can_view_related = False

        hazard_field = form.base_fields.get("hazard")
        if hazard_field:
            hazard_field.widget.can_add_related = False
            hazard_field.widget.can_change_related = False
            hazard_field.widget.can_delete_related = False
            hazard_field.widget.can_view_related = False
        return form


admin.site.register(AlertList, AlertListAdmin)
