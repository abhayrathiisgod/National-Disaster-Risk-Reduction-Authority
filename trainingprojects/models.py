from django.db import models
from django.contrib.auth.models import User
from federal.models import Province, District


class Address(models.Model):
    local_address = models.TextField()
    local_address_ne = models.TextField()

    def __str__(self) -> str:
        return self.local_address


class Donater(models.Model):
    donater_created_at = models.DateTimeField()
    donater_updated_at = models.DateTimeField()
    donater_deleted_at = models.DateTimeField(blank=True, null=True)
    name = models.TextField()
    icon = models.ImageField(upload_to='uploads/donater/icon')
    link = models.URLField()
    donater_created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_donaters')
    donater_updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_donaters')

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    donor = models.ForeignKey(Donater, on_delete=models.CASCADE)
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
        User, on_delete=models.CASCADE, related_name='created_projects')
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, related_name='updated_projects')
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.title
