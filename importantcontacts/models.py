from django.db import models
from django.db.models import Max
from federal.models import Province, District, Municipality

# Province Wise Focal Person Contact List


class ProvinceWiseFocalPersonContactList(models.Model):

    id = models.AutoField(primary_key=True)
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
    district = models.ForeignKey(District, on_delete=models.PROTECT)

# Local Disaster Management Contact List


class LocalDisasterManagementContactList(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    contact_num = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    municcipality = models.ForeignKey(
        Municipality, on_delete=models.PROTECT)

# snake bitess


class SnakeBites(models.Model):
    id = models.AutoField(primary_key=True)
    treatment_centre = models.CharField(max_length=255)
    treatment_centre_ne = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.PROTECT)


class EmergencyVehicle(models.Model):
    id = models.AutoField(primary_key=True)
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
    condition = models.TextField()
    province = models.ForeignKey(
        Province, on_delete=models.PROTECT, blank=True)
    district = models.ForeignKey(
        District, on_delete=models.PROTECT, blank=True)
    municipality = models.ForeignKey(
        Municipality, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.vehicle_type
