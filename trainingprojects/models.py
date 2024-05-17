from django.db import models
from django.contrib.auth.models import User
from federal.models import Province, District, Municipality
from django.core.validators import FileExtensionValidator
from django_filters.rest_framework import DjangoFilterBackend
from django_ckeditor_5.fields import CKEditor5Field


class Address(models.Model):
    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
    local_address = models.TextField()
    local_address_ne = models.TextField()

    def __str__(self) -> str:
        return self.local_address


class Donater(models.Model):
    donater_created_at = models.DateTimeField(blank=True, null=True)
    donater_updated_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='uploads/donater/icon', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])
    link = models.URLField()
    donater_created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=True, null=True, related_name='created_donaters')
    donater_updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_donaters')

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    donor = models.ForeignKey(Donater, on_delete=models.PROTECT)
    created_at = models.DateTimeField(blank=True, null=True,)
    updated_at = models.DateTimeField(blank=True, null=True,)
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    budget = models.CharField(max_length=50)
    budget_ne = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='created_projects')
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=True, null=True, related_name='updated_projects')
    province = models.ForeignKey(
        Province, on_delete=models.PROTECT, blank=True, null=True)
    district = models.ForeignKey(
        District, on_delete=models.PROTECT, blank=True, null=True)
    municipality = models.ForeignKey(
        Municipality, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class Training(models.Model):
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    num_of_participants = models.IntegerField()
    description = CKEditor5Field('Description', config_name='extends')
    description = CKEditor5Field('Description_ne', config_name='extends')
    attendants = models.CharField(max_length=255, blank=True, null=True)
    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    municipality = models.ForeignKey(
        Municipality, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self) -> str:
        return self.title


class fiscal(models.Model):
    year = models.CharField(max_length=255)
    year_ne = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.year


class GeoHazardAssessment(models.Model):
    fiscal_year = models.ForeignKey(fiscal, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    file = models.FileField(blank=True, null=True,
                            upload_to='uploads/geohazardassessment/')
    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    municipality = models.ForeignKey(
        Municipality, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self) -> str:
        return self.title
