from django.contrib import admin
from .models import Address, Donater, Project

# Register your models here.

admin.site.register(Address)
admin.site.register(Donater)
admin.site.register(Project)
