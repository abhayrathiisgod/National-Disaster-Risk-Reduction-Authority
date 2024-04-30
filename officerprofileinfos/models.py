from django.db import models

# Create your models here.


class Skills(models.Mode):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=255)
    title_ne = models.TextField(max_length=255)
    color = models.CharField(max_length=100)


class Designation(models.Model):
    id = models.IntegerField(primary_key=True)
    designation = models.CharField(max_length=200, blank=True, null=True)
    designation_ne = models.CharField(max_length=200, blank=True, null=True)
    office = models.CharField(max_length=100, blank=True, null=True)
    office_ne = models.CharField(max_length=100, blank=True, null=True)
    is_executive_committee = models.BooleanField(default=False)
    is_national_council = models.BooleanField(default=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.designation


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=255)
    title_ne = models.TextField(max_length=255)


class TrainingOrg(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=255)
    title_ne = models.TextField(max_length=255)


class TrainingCertificate(models.Model):
    id = models.AutoField(primary_key=True)
    certificate = models.URLField()


class Trainings(models.Model):
    id = models.AutoField(primary_key=True)
    training_org = models.ForeignKey(TrainingOrg, on_delete=models.DO_NOTHING)
    training_certificate = models.ManyToManyField(TrainingCertificate)
    title = models.TextField(max_length=255)
    title_ne = models.TextField(max_length=255)
    description = models.TextField()
    description_ne = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()


class OfficerProfile(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.ForeignKey(Designation, on_delete=models.DO_NOTHING)
    departments = models.ManyToManyField(Department)
    skills = models.ManyToManyField(Skills)
    trainings = models.ManyToManyField(Trainings)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    additional_info = models.TextField()
    additional_info_ne = models.TextField()
    image = models.ImageField()
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)
    order = models.IntegerField()

    def __str__(self):
        return self.name


class CommiteProfile(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.ForeignKey(Designation, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    additional_info = models.TextField()
    additional_info_ne = models.TextField()
    image = models.ImageField()
    order = models.IntegerField()


class NationalCouncilHead(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.ForeignKey(Designation, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    image = models.ImageField()


class ExecutiveCommitteHead(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.ForeignKey(Designation, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    image = models.ImageField()


class OfficersHead(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.ForeignKey(Designation, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    image = models.ImageField()


class OfficersSpokesPerson(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.ForeignKey(Designation, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    image = models.ImageField()


class InformationOfficer(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.ForeignKey(Designation, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    image = models.ImageField()