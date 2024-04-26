from django.db import models
from federal.models import Ward

# Create your models here.


class AlertList(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    wards = models.ManyToManyField(Ward)
   # points = models.ManyToManyField() --almost done
    description = models.TextField()
    verified = models.BooleanField(default=False)
    public = models.BooleanField(default=False)
    startedon = models.DateTimeField()
    expireon = models.DateTimeField(blank=True, null=True)
    referenceType = models.CharField(max_length=255)
    # ref data
    # ref id
    created_by = models.CharField(max_length=255)
    updated_by = models.CharField(max_length=255)
