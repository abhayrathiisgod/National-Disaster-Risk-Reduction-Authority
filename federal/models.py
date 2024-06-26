from django.db import models
from django.db.models import Max
from django_ckeditor_5.fields import CKEditor5Field


class Province(models.Model):

    class Meta:
        verbose_name = "Province"
        verbose_name_plural = "Provinces"

    province_name = models.CharField(max_length=100)
    province_name_ne = models.CharField(max_length=100)
    code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self) -> str:
        return self.province_name


class District(models.Model):

    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"

    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    district_name = models.CharField(max_length=100)
    district_name_ne = models.CharField(max_length=100)
    code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self) -> str:
        return self.district_name


class Municipality(models.Model):

    class Meta:
        verbose_name = "Municipality"
        verbose_name_plural = "Municipalities"

    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    municipality_name = models.CharField(max_length=100)
    municipality_name_ne = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.municipality_name

    def save(self, *args, **kwargs):

        if not self.id:
            max_id = type(self).objects.filter(
                district=self.district).aggregate(Max('id'))['id__max']
            next_id = (self.district_id * 1000) + \
                1 if max_id is None else max_id + 1
            self.id = next_id

        super().save(*args, **kwargs)


class Ward(models.Model):

    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    municipality = models.ForeignKey(Municipality, on_delete=models.PROTECT)
    ward_name = models.CharField(max_length=100)
    ward_name_ne = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.ward_name

    def save(self, *args, **kwargs):
        if not self.id:
            max_id = type(self).objects.filter(
                district=self.district).aggregate(Max('id'))['id__max']
            next_id = (self.district_id * 100) + \
                1 if max_id is None else max_id + 1
            self.id = next_id
        super().save(*args, **kwargs)
