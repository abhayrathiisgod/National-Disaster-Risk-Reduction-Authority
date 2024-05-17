from django.contrib import admin
from importantcontacts.models import MohaPhoneDirectoryList, ProvinceWiseFocalPersonContactList, DeocHeadList, LocalDisasterManagementContactList, MohaSubordinateList, SnakeBites, EmergencyVehicle
from django.contrib.admin.options import TabularInline


class ProvinceWiseFocalPersonContactListAdmin(admin.ModelAdmin):
    actions = None
    list_display = (
        'id', 'province', 'designation', 'govt_contact_person_name',
        'govt_contact_person_mobile', 'province_focal_point_agency',
        'agency_contact_person_name', 'agency_contact_person_mobile'
    )
    list_display_links = (
        'id', 'province', 'designation', 'govt_contact_person_name',
        'govt_contact_person_mobile', 'province_focal_point_agency',
        'agency_contact_person_name', 'agency_contact_person_mobile'
    )
    search_fields = ('designation', 'govt_contact_person_name')
    list_filter = ('province',)

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


class MohaPhoneDirectoryListAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'division_section', 'phone', 'mobile', 'email')
    list_display_links = ('id', 'division_section', 'phone', 'mobile', 'email')
    search_fields = ('division_section',)

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


class MohaSubordinateListAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'name', 'address', 'phone')
    list_display_links = ('id', 'name', 'address', 'phone')
    search_fields = ('name', 'address')

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


class DeocHeadListAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'designation', 'office_landline_no', 'district')
    list_display_links = ('id', 'designation',
                          'office_landline_no', 'district')
    search_fields = ('designation',)

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


class LocalDisasterManagementContactListAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'email', 'contact_num',
                    'province', 'district', 'municcipality')
    list_display_links = ('id', 'email', 'contact_num',
                          'province', 'district', 'municcipality')
    search_fields = ('email', 'contact_num')
    list_filter = ('province', 'district', 'municcipality')

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


class SnakeBitesAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'treatment_centre', 'district')
    list_display_links = ('id', 'treatment_centre', 'district')
    search_fields = ('treatment_centre',)
    list_filter = ('district',)

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


class EmergencyVehicleAdmin(admin.ModelAdmin):
    actions = None
    list_display = ('id', 'vehicle_type', 'ownership', 'vechicle_no',
                    'driver_name', 'province', 'district', 'municipality')
    list_display_links = ('id', 'vehicle_type', 'ownership', 'vechicle_no',
                          'driver_name', 'province', 'district', 'municipality')
    search_fields = ('vehicle_type', 'ownership', 'vechicle_no', 'driver_name')
    list_filter = ('province', 'district', 'municipality')

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


# Register the admin classes
admin.site.register(ProvinceWiseFocalPersonContactList,
                    ProvinceWiseFocalPersonContactListAdmin)
admin.site.register(MohaPhoneDirectoryList, MohaPhoneDirectoryListAdmin)
admin.site.register(MohaSubordinateList, MohaSubordinateListAdmin)
admin.site.register(DeocHeadList, DeocHeadListAdmin)
admin.site.register(LocalDisasterManagementContactList,
                    LocalDisasterManagementContactListAdmin)
admin.site.register(SnakeBites, SnakeBitesAdmin)
admin.site.register(EmergencyVehicle, EmergencyVehicleAdmin)
