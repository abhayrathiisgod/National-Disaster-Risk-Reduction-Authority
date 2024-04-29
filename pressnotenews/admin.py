from django.contrib import admin
from pressnotenews.models import NewsInfo, Author, Type, PressNote

# Register your models here.
admin.site.register(Author)
admin.site.register(Type)
admin.site.register(NewsInfo)
admin.site.register(PressNote)
