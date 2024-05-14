from django.db import models
from django.contrib.auth.models import User
from federal.models import Province, District, Municipality
from django.core.validators import FileExtensionValidator
from django_filters.rest_framework import DjangoFilterBackend
from django_ckeditor_5.fields import CKEditor5Field


class Address(models.Model):
    local_address = models.TextField()
    local_address_ne = models.TextField()

    def __str__(self) -> str:
        return self.local_address


class Donater(models.Model):
    donater_created_at = models.DateTimeField()
    donater_updated_at = models.DateTimeField()
    donater_deleted_at = models.DateTimeField(blank=True, null=True)
    name = CKEditor5Field('Text', config_name='extends')
    icon = models.ImageField(upload_to='uploads/donater/icon', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])
    link = models.URLField()
    donater_created_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='created_donaters')
    donater_updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_donaters')

    def __str__(self) -> str:
        return self.name

    def delete(self, *args, **kwargs):
        self.icon.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = Donater.objects.get(pk=self.pk)
            if self.icon != old_instance.icon:
                old_instance.icon.delete(save=False)

        super(Donater, self).save(*args, **kwargs)


class Project(models.Model):
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    donor = models.ForeignKey(Donater, on_delete=models.PROTECT)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)
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
    district = models.ForeignKey(District, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.title


class Training(models.Model):
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    num_of_participants = models.IntegerField()
    description = CKEditor5Field('Text', config_name='extends')
    description = CKEditor5Field('Text', config_name='extends')
    attendants = models.CharField(max_length=255, blank=True, null=True)
    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    municipality = models.ForeignKey(
        Municipality, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self) -> str:
        return self.title
