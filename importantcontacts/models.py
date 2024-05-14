from django.db import models
from django.db.models import Max
from federal.models import Province, District, Municipality
from django_ckeditor_5.fields import CKEditor5Field

# Province Wise Focal Person Contact List


class ProvinceWiseFocalPersonContactList(models.Model):
    province = models.ForeignKey(Province, on_delete=models.PROTECT)
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
    division_section = CKEditor5Field('Text', config_name='extends')
    division_section_ne = CKEditor5Field('Text', config_name='extends')
    phone = models.CharField(blank=True, max_length=255)
    mobile = models.CharField(blank=True, max_length=255)
    email = models.EmailField(blank=True)

# Moha Subordinate List


class MohaSubordinateList(models.Model):
    name = CKEditor5Field('Text', config_name='extends')
    name_ne = CKEditor5Field('Text', config_name='extends')
    address = CKEditor5Field('Text', config_name='extends')
    address_ne = CKEditor5Field('Text', config_name='extends')
    phone = CKEditor5Field('Text', config_name='extends', blank=True)

# Deoc Head List


class DeocHeadList(models.Model):
    designation = models.CharField(max_length=255)
    designation_ne = models.CharField(max_length=255)
    office_landline_no = models.CharField(max_length=255)
    fax_no = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.PROTECT)

# Local Disaster Management Contact List


class LocalDisasterManagementContactList(models.Model):
    email = models.EmailField()
    contact_num = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    municcipality = models.ForeignKey(
        Municipality, on_delete=models.PROTECT)

# snake bitess


class SnakeBites(models.Model):
    treatment_centre = models.CharField(max_length=255)
    treatment_centre_ne = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.PROTECT)


class EmergencyVehicle(models.Model):
    type = (
        ('Ambulance', 'Ambulance'),
        ('Fire_truck', 'Fire_truck'),
        ('Police_vehicle', 'Police_vehicle'),
    )
    vehicle_type = models.CharField(max_length=255, choices=type)
    ownership = models.CharField(max_length=255, blank=True)
    ownership_ne = models.CharField(max_length=255, blank=True)
    vechicle_no = models.CharField(max_length=255, blank=True)
    vechicle_no_ne = models.CharField(max_length=255, blank=True)
    driver_name = models.CharField(max_length=255, blank=True)
    driver_name_ne = models.CharField(max_length=255, blank=True)
    contact = models.CharField(max_length=255, blank=True)
    alt_contact = models.CharField(max_length=255, blank=True)
    condition = CKEditor5Field('Text', config_name='extends')
    province = models.ForeignKey(
        Province, on_delete=models.PROTECT, blank=True)
    district = models.ForeignKey(
        District, on_delete=models.PROTECT, blank=True)
    municipality = models.ForeignKey(
        Municipality, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.vehicle_type
