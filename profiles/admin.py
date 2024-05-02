from django.contrib import admin
from .models import Skills, Designation, Department, TrainingOrg, TrainingCertificate, Trainings, OfficerProfile, CommiteProfile, NationalCouncilHead, ExecutiveCommitteHead, OfficersHead, OfficersSpokesPerson, InformationOfficer


class BaseAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None) -> bool:
        return request.user.is_superuser


class SkillsAdmin(BaseAdmin):
    list_display = ('title', 'title_ne', 'color')
    list_display_links = ('title', 'title_ne', 'color')
    search_fields = ('title', 'title_ne')


class DesignationAdmin(BaseAdmin):
    list_display = ('designation', 'designation_ne', 'office',
                    'office_ne', 'is_executive_committee', 'is_national_council')
    list_display_links = ('designation', 'designation_ne', 'office',
                          'office_ne', 'is_executive_committee', 'is_national_council')
    list_filter = ('is_executive_committee', 'is_national_council')
    search_fields = ('designation', 'designation_ne', 'office', 'office_ne')


class DepartmentAdmin(BaseAdmin):
    list_display = ('title', 'title_ne')
    list_display_links = ('title', 'title_ne')
    search_fields = ('title', 'title_ne')


class TrainingOrgAdmin(BaseAdmin):
    list_display = ('title', 'title_ne')
    list_display_links = ('title', 'title_ne')
    search_fields = ('title', 'title_ne')


class TrainingCertificateAdmin(BaseAdmin):
    list_display = ('certificate',)
    list_display_links = ('certificate',)
    search_fields = ('certificate',)


class TrainingsAdmin(BaseAdmin):
    list_display = ('training_org', 'title', 'title_ne',
                    'start_date', 'end_date')
    list_display_links = ('training_org', 'title', 'title_ne',
                          'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('training_org__title', 'title',
                     'title_ne', 'description', 'description_ne')


class OfficerProfileAdmin(BaseAdmin):
    list_display = ('name', 'name_ne', 'designation',
                    'from_date', 'to_date', 'order')
    list_display_links = ('name', 'name_ne', 'designation',
                          'from_date', 'to_date', 'order')
    list_filter = ('designation__designation', 'from_date', 'to_date')
    search_fields = ('name', 'name_ne', 'designation__designation',
                     'mobile', 'email', 'additional_info', 'additional_info_ne')


class CommiteProfileAdmin(BaseAdmin):
    list_display = ('name', 'name_ne', 'designation', 'order')
    list_display_links = ('name', 'name_ne', 'designation', 'order')
    list_filter = ('order',)
    search_fields = ('name', 'name_ne', 'designation__designation')


class NationalCouncilHeadAdmin(BaseAdmin):
    list_display = ('name', 'name_ne', 'designation', 'order')
    list_display_links = ('name', 'name_ne', 'designation', 'order')
    list_filter = ('order',)
    search_fields = ('name', 'name_ne', 'designation__designation')


class ExecutiveCommitteHeadAdmin(BaseAdmin):
    list_display = ('name', 'name_ne', 'designation', 'order')
    list_display_links = ('name', 'name_ne', 'designation', 'order')
    list_filter = ('order',)
    search_fields = ('name', 'name_ne', 'designation__designation')


class OfficersHeadAdmin(BaseAdmin):
    list_display = ('name', 'name_ne', 'designation', 'order')
    list_display_links = ('name', 'name_ne', 'designation', 'order')
    list_filter = ('order',)
    search_fields = ('name', 'name_ne', 'designation__designation')


class OfficersSpokesPersonAdmin(BaseAdmin):
    list_display = ('name', 'name_ne', 'designation', 'order')
    list_display_links = ('name', 'name_ne', 'designation', 'order')
    list_filter = ('order',)
    search_fields = ('name', 'name_ne', 'designation__designation')


class InformationOfficerAdmin(BaseAdmin):
    list_display = ('name', 'name_ne', 'designation', 'order')
    list_display_links = ('name', 'name_ne', 'designation', 'order')
    list_filter = ('order',)
    search_fields = ('name', 'name_ne', 'designation__designation')


admin.site.register(Skills, SkillsAdmin)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(TrainingOrg, TrainingOrgAdmin)
admin.site.register(TrainingCertificate, TrainingCertificateAdmin)
admin.site.register(Trainings, TrainingsAdmin)
admin.site.register(OfficerProfile, OfficerProfileAdmin)
admin.site.register(CommiteProfile, CommiteProfileAdmin)
admin.site.register(NationalCouncilHead, NationalCouncilHeadAdmin)
admin.site.register(ExecutiveCommitteHead, ExecutiveCommitteHeadAdmin)
admin.site.register(OfficersHead, OfficersHeadAdmin)
admin.site.register(OfficersSpokesPerson, OfficersSpokesPersonAdmin)
admin.site.register(InformationOfficer, InformationOfficerAdmin)
