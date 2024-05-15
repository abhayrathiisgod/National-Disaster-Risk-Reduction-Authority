from django.db import models
from profiles.models import OfficerProfile
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.


class ImportantLinks(models.Model):
    class Meta:
        verbose_name = "Important Link"
        verbose_name_plural = "Important Link List"
    name = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.name


class BipadAlerts(models.Model):
    class Meta:
        verbose_name = "Bipad Alert"
        verbose_name_plural = "Bipad Alert List"

    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    description = CKEditor5Field(
        'Text', config_name='extends', null=True, blank=True)
    description_ne = CKEditor5Field(
        'Text', config_name='extends', null=True, blank=True)
    important_links = models.ManyToManyField(ImportantLinks)
    important_numbers = models.ManyToManyField(OfficerProfile)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
