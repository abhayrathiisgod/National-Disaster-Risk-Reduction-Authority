from django.db import models
import os


class Designation(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=100)
    designation_ne = models.CharField(max_length=100)
    office = models.CharField(max_length=100)
    office_ne = models.CharField(max_length=100)
    is_executive_committee = models.BooleanField(default=False)
    is_national_council = models.BooleanField(default=False)
    link = models.URLField()

    def __str__(self) -> str:
        return self.designation


def get_upload_path_officer(instance, filename):
    return os.path.join('uploads/officer', instance.name, filename)


class Officer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    name_ne = models.CharField(max_length=255)
    additional_info = models.TextField()
    additional_info_ne = models.TextField()
    image = models.ImageField(upload_to=get_upload_path_officer)
    order = models.IntegerField()
    designations = models.ForeignKey(Designation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Leadership(models.Model):
    officer_head = models.ForeignKey(Officer, on_delete=models.DO_NOTHING)


class NationalCouncilHead(Leadership):
    pass


class ExecutiveCommitteeHead(Leadership):
    pass


class OfficersHead(Leadership):
    pass


class OfficersSpokesperson(Leadership):
    pass


class InformationOfficer(Leadership):
    pass
