from django.contrib import admin
from .models import PublicationAuthor, Publications, PublicationType

# Register your models here.

admin.site.register(PublicationAuthor)
admin.site.register(Publications)
admin.site.register(PublicationType)
