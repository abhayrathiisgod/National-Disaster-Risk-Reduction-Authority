from django.contrib import admin
from bulletin.models import Bulletin, BulletinAuthor, BulletinType

# Register your models here.
admin.site.register(Bulletin)
admin.site.register(BulletinAuthor)
admin.site.register(BulletinType)
