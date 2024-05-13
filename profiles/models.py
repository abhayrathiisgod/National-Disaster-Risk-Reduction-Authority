from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class Skills(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=255)
    title_ne = models.TextField(max_length=255)
    color = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Designation(models.Model):
    id = models.AutoField(primary_key=True)
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
    title = models.TextField(max_length=255, unique=True)
    title_ne = models.TextField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.title


class TrainingOrg(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=255, unique=True)
    title_ne = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.title


class TrainingCertificate(models.Model):
    id = models.AutoField(primary_key=True)
    certificate = models.URLField()

    def __str__(self) -> str:
        return self.certificate


class Trainings(models.Model):
    id = models.AutoField(primary_key=True)
    training_org = models.ForeignKey(TrainingOrg, on_delete=models.PROTECT)
    training_certificate = models.ManyToManyField(TrainingCertificate)
    title = models.TextField(max_length=255, unique=True)
    title_ne = models.TextField(max_length=255)
    description = models.TextField()
    description_ne = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return self.title


class OfficerProfile(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    departments = models.ManyToManyField(Department)
    skills = models.ManyToManyField(Skills)
    trainings = models.ManyToManyField(Trainings, blank=True, null=True)
    name = models.CharField(max_length=100, unique=True)
    name_ne = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    additional_info = models.TextField()
    additional_info_ne = models.TextField()
    image = models.ImageField(upload_to='uploads/profiles/prof', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):

        if self.pk:
            old_instance = OfficerProfile.objects.get(pk=self.pk)
            if self.image != old_instance.image:
                old_instance.image.delete(save=False)

        super(OfficerProfile, self).save(*args, **kwargs)


class CommiteProfile(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    additional_info = models.TextField(blank=True, null=True)
    additional_info_ne = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/profiles/prof', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])
    order = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):

        if self.pk:
            old_instance = CommiteProfile.objects.get(pk=self.pk)
            if self.image != old_instance.image:
                old_instance.image.delete(save=False)

        super(CommiteProfile, self).save(*args, **kwargs)


class NationalCouncilHead(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    additional_info = models.TextField(blank=True, null=True)
    additional_info_ne = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/profiles/prof', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])
    order = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):

        if self.pk:
            old_instance = NationalCouncilHead.objects.get(pk=self.pk)
            if self.image != old_instance.image:
                old_instance.image.delete(save=False)

        super(NationalCouncilHead, self).save(*args, **kwargs)


class ExecutiveCommitteHead(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    additional_info = models.TextField(blank=True, null=True)
    additional_info_ne = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/profiles/prof', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])
    order = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):

        if self.pk:
            old_instance = ExecutiveCommitteHead.objects.get(pk=self.pk)
            if self.image != old_instance.image:
                old_instance.image.delete(save=False)

        super(ExecutiveCommitteHead, self).save(*args, **kwargs)


class OfficersHead(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    additional_info = models.TextField(blank=True, null=True)
    additional_info_ne = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/profiles/prof', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])
    order = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):

        if self.pk:
            old_instance = OfficersHead.objects.get(pk=self.pk)
            if self.image != old_instance.image:
                old_instance.image.delete(save=False)

        super(OfficersHead, self).save(*args, **kwargs)


class OfficersSpokesPerson(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    additional_info = models.TextField(blank=True, null=True)
    additional_info_ne = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/profiles/prof', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])
    order = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):

        if self.pk:
            old_instance = OfficersSpokesPerson.objects.get(pk=self.pk)
            if self.image != old_instance.image:
                old_instance.image.delete(save=False)

        super(OfficersSpokesPerson, self).save(*args, **kwargs)


class InformationOfficer(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    additional_info = models.TextField(blank=True, null=True)
    additional_info_ne = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/profiles/prof', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])
    order = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):

        if self.pk:
            old_instance = InformationOfficer.objects.get(pk=self.pk)
            if self.image != old_instance.image:
                old_instance.image.delete(save=False)

        super(InformationOfficer, self).save(*args, **kwargs)
