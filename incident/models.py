from django.utils import timezone
from django.db import models
from federal.models import Ward
from django.contrib.auth.models import User
from hazard.models import Hazards


class Loss(models.Model):
    id = models.AutoField(primary_key=True)
    peopleDeathCount = models.IntegerField(default=0)
    peopleDeathMaleCount = models.IntegerField(default=0)
    peopleDeathFemaleCount = models.IntegerField(default=0)
    peopleDeathOtherCount = models.IntegerField(default=0)
    peopleDeathUnknownCount = models.IntegerField(default=0)
    peopleDeathDisabledCount = models.IntegerField(default=0)
    peopleMissingCount = models.IntegerField(default=0)
    peopleMissingMaleCount = models.IntegerField(default=0)
    peopleMissingFemaleCount = models.IntegerField(default=0)
    peopleMissingOtherCount = models.IntegerField(default=0)
    peopleMissingUnknownCount = models.IntegerField(default=0)
    peopleMissingDisabledCount = models.IntegerField(default=0)
    peopleInjuredCount = models.IntegerField(default=0)
    peopleInjuredMaleCount = models.IntegerField(default=0)
    peopleInjuredFemaleCount = models.IntegerField(default=0)
    peopleInjuredOtherCount = models.IntegerField(default=0)
    peopleInjuredUnknownCount = models.IntegerField(default=0)
    peopleInjuredDisabledCount = models.IntegerField(default=0)
    peopleAffectedCount = models.IntegerField(default=0)
    familyAffectedCount = models.IntegerField(default=0)
    familyRelocatedCount = models.IntegerField(default=0)
    familyEvacuatedCount = models.IntegerField(default=0)
    livestockDestroyedCount = models.IntegerField(default=0)
    infrastructureDestroyedCount = models.IntegerField(default=0)
    infrastructureDestroyedHouseCount = models.IntegerField(default=0)
    infrastructureAffectedHouseCount = models.IntegerField(default=0)
    infrastructureDestroyedRoadCount = models.IntegerField(default=0)
    infrastructureAffectedRoadCount = models.IntegerField(default=0)
    infrastructureDestroyedBridgeCount = models.IntegerField(default=0)
    infrastructureAffectedBridgeCount = models.IntegerField(default=0)
    infrastructureDestroyedElectricityCount = models.IntegerField(default=0)
    infrastructureAffectedElectricityCount = models.IntegerField(default=0)
    infrastructureEconomicLoss = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    agricultureEconomicLoss = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    createdOn = models.DateTimeField()
    modifiedOn = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    estimatedLoss = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Loss {self.id}"


class Incident(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    point = models.CharField(max_length=255)
    createdOn = models.DateTimeField(default=timezone.now())
    modifiedOn = models.DateTimeField(default=timezone.now())
    titleNe = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    cause = models.TextField(null=True, blank=True)
    verified = models.BooleanField(default=False)
    verificationMessage = models.TextField(null=True, blank=True)
    approved = models.BooleanField(default=False)
    polygon = models.CharField(max_length=255, null=True, blank=True)
    incidentOn = models.DateTimeField()
    reportedOn = models.DateTimeField()
    streetAddress = models.CharField(max_length=255)
    detail = models.TextField(null=True, blank=True)
    needFollowup = models.BooleanField(default=False)
    region = models.CharField(max_length=255, null=True, blank=True)
    regionId = models.IntegerField(null=True, blank=True)
    dataSourceId = models.IntegerField()
    dataSource = models.CharField(max_length=255)
    source_TYPES = [
        ('Nepal_police', 'Nepal_police'),
        ('Initial Rapid Assessment', 'Initial_Rapid_Assessment'),
        ('Other', 'Other'),

    ]
    source = models.CharField(choices=source_TYPES, null=True, blank=True)
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
    hazard = models.ForeignKey(Hazards, on_delete=models.PROTECT)
    loss = models.ForeignKey(
        Loss, on_delete=models.CASCADE, null=True, blank=True)
    createdBy = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='incidents_created', null=True, blank=True)
    updatedBy = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='incidents_updated', null=True, blank=True)

    wards = models.ManyToManyField(Ward)

    def __str__(self):
        return self.title
