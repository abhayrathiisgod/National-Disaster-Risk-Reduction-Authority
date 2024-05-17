from django.contrib import admin
from .models import Address, Donater, Project, Training, fiscal, GeoHazardAssessment


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'local_address', 'local_address_ne')
    list_display_links = ('id', 'local_address', 'local_address_ne')
    search_fields = ('local_address',)

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


class fiscalAdmin(admin.ModelAdmin):
    list_display = ('id', 'year', 'year_ne')
    list_display_links = ('id', 'year', 'year_ne')
    search_fields = ('year',)

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


class GeoHazardAssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'fiscal_year', 'title')
    list_display_links = ('id', 'fiscal_year', 'title')
    search_fields = ('title',)
    list_filter = ('province', 'district')

    def get_form(self, request, obj=None, **kwargs):
        form = super(GeoHazardAssessmentAdmin, self).get_form(
            request, obj, **kwargs)

        address_field = form.base_fields.get("fiscal_year")
        if address_field:
            address_field.widget.can_add_related = True
            address_field.widget.can_change_related = False
            address_field.widget.can_delete_related = False
            address_field.widget.can_view_related = False

        return form

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
    readonly_fields = ('donater_created_at', 'donater_updated_at')

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
                    'end_date', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'budget', 'start_date',
                          'end_date', 'created_at', 'updated_at')
    list_filter = ('start_date', 'end_date', 'created_at',
                   'updated_at')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')

    def get_form(self, request, obj=None, **kwargs):
        form = super(ProjectAdmin, self).get_form(request, obj, **kwargs)

        address_field = form.base_fields.get("address")
        if address_field:
            address_field.widget.can_add_related = True
            address_field.widget.can_change_related = False
            address_field.widget.can_delete_related = False
            address_field.widget.can_view_related = False

        Donor_field = form.base_fields.get("donor")
        if Donor_field:
            Donor_field.widget.can_add_related = False
            Donor_field.widget.can_change_related = False
            Donor_field.widget.can_delete_related = False
            Donor_field.widget.can_view_related = False
        return form

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
    list_display = ('title', 'startDate', 'endDate',
                    'num_of_participants', 'province', 'district', 'municipality')
    list_display_links = ('title',)
    list_filter = ('province', 'district', 'startDate', 'endDate')
    search_fields = ('title',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(TrainingAdmin, self).get_form(request, obj, **kwargs)

        address_field = form.base_fields.get("address")
        if address_field:
            address_field.widget.can_add_related = True
            address_field.widget.can_change_related = False
            address_field.widget.can_delete_related = False
            address_field.widget.can_view_related = False

        return form

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
admin.site.register(fiscal, fiscalAdmin)
admin.site.register(GeoHazardAssessment, GeoHazardAssessmentAdmin)
