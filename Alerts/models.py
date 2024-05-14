from django.db import models
from hazard.models import Hazards
from django.contrib.auth.models import User
from federal.models import Ward
from django.utils.timezone import now
from django_ckeditor_5.fields import CKEditor5Field


class AlertList(models.Model):
    title = models.CharField(max_length=255)
    wards = models.ForeignKey(Ward, on_delete=models.PROTECT, default=101)
    point = models.CharField()
    createdOn = models.DateTimeField(default=now)
    titleNe = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    description = CKEditor5Field('Text', config_name='extends')
    verified = models.BooleanField(default=False)
    public = models.BooleanField(default=False)
    startedOn = models.DateTimeField()
    expireOn = models.DateTimeField(null=True, blank=True)
    polygon = models.CharField(null=True, blank=True)
    referenceType = models.CharField(max_length=255)
    referenceData = models.TextField()
    referenceId = models.IntegerField()
    region = models.CharField(max_length=255, null=True, blank=True)
    regionId = models.IntegerField(null=True, blank=True)
    createdBy = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='%(class)s_created', null=True, blank=True)
    updatedBy = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='%(class)s_updated', null=True, blank=True)
    hazard = models.ForeignKey(Hazards, on_delete=models.PROTECT)
    DISASTER_TYPES = [
        ('Earthquake', 'Earthquake'),
        ('Hurricane', 'Hurricane'),
        ('Tornado', 'Tornado'),
        ('Flood', 'Flood'),
        ('Wildfire', 'Wildfire'),
        ('Tsunami', 'Tsunami'),
        ('Volcanic eruption', 'Volcanic eruption'),
        ('Landslide', 'Landslide'),
        ('Drought', 'Drought'),
        ('Blizzard', 'Blizzard'),
        ('Heatwave', 'Heatwave'),
        ('Avalanche', 'Avalanche'),
        ('Cyclone', 'Cyclone'),
        ('Thunderstorm', 'Thunderstorm'),
        ('Hailstorm', 'Hailstorm'),
    ]

    event = models.CharField(choices=DISASTER_TYPES, null=True, blank=True)

    def __str__(self):
        return self.title
