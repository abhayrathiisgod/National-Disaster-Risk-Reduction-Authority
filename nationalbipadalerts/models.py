from django.db import models
from profiles.models import OfficerProfile

# Create your models here.


class ImportantLinks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    link = models.URLField()

    def __str__(self):
        return self.name


class BipadAlerts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    description = models.TextField()
    description_ne = models.TextField()
    important_links = models.ManyToManyField(ImportantLinks)
    important_numbers = models.ManyToManyField(OfficerProfile)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
