from django.contrib import admin
from website.models import Page, ContactDetail, Introduction, WardDocument, FrequentlyAskedQuestions

# Register your models here.

admin.site.register(ContactDetail)
admin.site.register(Page)
admin.site.register(Introduction)
admin.site.register(WardDocument)
admin.site.register(FrequentlyAskedQuestions)
