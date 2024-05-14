from django.contrib import admin
from django.http import HttpRequest
from federal.models import Province, District, Municipality, Ward

# Register your models here.


class ProvinceAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'province_name', 'code')
    list_display_links = ('id', 'province_name', 'code')
    list_filter = ('province_name', 'code')
    search_fields = ('province_name',)

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False


class DistrictAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'district_name', 'code')
    list_display_links = ('id', 'district_name', 'code')
    list_filter = ('province__province_name', 'code')
    search_fields = ('district_name',)

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False


class MunicipalityAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'municipality_name', 'district', 'province')
    list_display_links = ('id', 'municipality_name', 'district', 'province')
    list_filter = ('district__district_name', 'province__province_name')
    search_fields = ('municipality_name',)

    def has_delete_permission(self, request, obj=None) -> bool:
        return False

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False


class WardAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'ward_name', 'municipality', 'district', 'province')
    list_display_links = (
        'id', 'ward_name', 'municipality', 'district', 'province')
    list_filter = ('id', 'municipality__municipality_name',
                   'district__district_name', 'province__province_name')
    search_fields = ('ward_name',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def get_form(self, request, obj=None, **kwargs):
        form = super(WardAdmin, self).get_form(request, obj, **kwargs)

        municipality_field = form.base_fields.get("municipality")
        if municipality_field:
            municipality_field.widget.can_add_related = False
            municipality_field.widget.can_change_related = False
            municipality_field.widget.can_delete_related = False

        return form


admin.site.register(Province, ProvinceAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Ward, WardAdmin)
