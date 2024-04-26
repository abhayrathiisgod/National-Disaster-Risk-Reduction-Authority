from django.db import models
from django.db.models import Max
from federal.models import Province, District, Municipality

# Province Wise Focal Person Contact List


class ProvinceWiseFocalPersonContactList(models.Model):

    id = models.AutoField(primary_key=True)
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING)
    designation = models.CharField(max_length=255)
    designation_ne = models.CharField(max_length=255)
    govt_contact_person_name = models.CharField(max_length=255)
    govt_contact_person_name_ne = models.CharField(
        max_length=255)
    govt_contact_person_mobile = models.CharField(max_length=255)
    govt_contact_person_email = models.EmailField()
    province_focal_point_agency = models.CharField(max_length=255)
    agency_contact_person_name = models.CharField(max_length=255)
    agency_contact_person_name_ne = models.CharField(
        max_length=255)
    agency_contact_person_mobile = models.CharField(max_length=255)
    agency_contact_person_email = models.EmailField()

    def __str__(self) -> str:
        return self.govt_contact_person_name

# Moha Phone Directory List


class MohaPhoneDirectoryList(models.Model):
    id = models.AutoField(primary_key=True)
    division_section = models.TextField()
    division_section_ne = models.TextField()
    phone = models.CharField(blank=True, max_length=255)
    mobile = models.CharField(blank=True, max_length=255)
    email = models.EmailField(blank=True)

# Moha Subordinate List


class MohaSubordinateList(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    name_ne = models.TextField()
    address = models.TextField()
    address_ne = models.TextField()
    phone = models.TextField(blank=True)

# Deoc Head List


class DeocHeadList(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=255)
    designation_ne = models.CharField(max_length=255)
    office_landline_no = models.CharField(max_length=255)
    fax_no = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING)

# Local Disaster Management Contact List


class LocalDisasterManagementContactList(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    contact_num = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING)
    municcipality = models.ForeignKey(
        Municipality, on_delete=models.DO_NOTHING)
