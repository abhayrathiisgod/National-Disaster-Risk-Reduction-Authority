from django.contrib import admin
from django.http import HttpRequest
from . import models

# Register your models here.


class ImportantLinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    list_display_links = ('name', 'link')
    search_fields = ('name', 'link')


class BipadAlertsAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_ne', 'description',
                    'description_ne', 'last_updated')
    list_display_links = ('title', 'title_ne', 'description',
                          'description_ne', 'last_updated')
    search_fields = ('title',)


admin.site.register(models.ImportantLinks, ImportantLinksAdmin)
admin.site.register(models.BipadAlerts, BipadAlertsAdmin)
