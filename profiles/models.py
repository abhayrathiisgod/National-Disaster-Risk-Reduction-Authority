from django.db import models
from django.core.validators import FileExtensionValidator
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.safestring import mark_safe


class Skills(models.Model):
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
    title = models.TextField(max_length=255)
    title_ne = models.TextField(max_length=255)
    color = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Designation(models.Model):
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
    title = models.TextField(max_length=255, unique=True)
    title_ne = models.TextField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.title


class TrainingOrg(models.Model):
    title = models.TextField(max_length=255, unique=True)
    title_ne = models.TextField(max_length=255)

    def __str__(self) -> str:
        return self.title


class TrainingCertificate(models.Model):
    certificate = models.URLField()

    def __str__(self) -> str:
        return self.certificate


class Trainings(models.Model):
    class Meta:
        verbose_name = "Training"
        verbose_name_plural = "Trainings"
    training_org = models.ForeignKey(TrainingOrg, on_delete=models.PROTECT)
    training_certificate = models.ManyToManyField(TrainingCertificate)
    title = models.TextField(max_length=255, unique=True)
    title_ne = models.TextField(max_length=255)
    description = CKEditor5Field('description', config_name='extends')
    description_ne = CKEditor5Field('description_ne', config_name='extends')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return self.title


class OfficerProfile(models.Model):
    class Meta:
        verbose_name = "Officer Profile"
        verbose_name_plural = "Officer Profile List"
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    departments = models.ManyToManyField(Department)
    skills = models.ManyToManyField(Skills)
    trainings = models.ManyToManyField(Trainings, blank=True)
    name = models.CharField(max_length=100, unique=True)
    name_ne = models.CharField(max_length=100)
    mobile = models.CharField(max_length=255)
    email = models.EmailField()
    additional_info = CKEditor5Field('additional_info', config_name='extends')
    additional_info_ne = CKEditor5Field(
        'additional_info_ne', config_name='extends')
    image = models.ImageField(upload_to='uploads/profiles/prof', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class CommiteProfile(models.Model):
    class Meta:
        verbose_name = "Committee Profile"
        verbose_name_plural = "Committee Profilee List"
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    additional_info = CKEditor5Field(
        'additional_info', config_name='extends', blank=True, null=True)
    additional_info_ne = CKEditor5Field(
        'additional_info_ne', config_name='extends', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/profiles/prof', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])
    order = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.name


class NationalCouncilHead(models.Model):
    class Meta:
        verbose_name = "National Council Head"
        verbose_name_plural = "National Council Head List"
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    additional_info = CKEditor5Field(
        'additional_info', config_name='extends', blank=True, null=True)
    additional_info_ne = CKEditor5Field(
        'additional_info_ne', config_name='extends', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/profiles/prof', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])
    order = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.name


class ExecutiveCommitteHead(models.Model):
    class Meta:
        verbose_name = "Executive Committee Head"
        verbose_name_plural = "Executive Committee Head List"
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    additional_info = CKEditor5Field(
        'additional_info', config_name='extends', blank=True, null=True)
    additional_info_ne = CKEditor5Field(
        'additional_info_ne', config_name='extends', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/profiles/prof', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])
    order = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.name


class OfficersHead(models.Model):
    class Meta:
        verbose_name = "Officers Head"
        verbose_name_plural = "Officers Head List"
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    additional_info = CKEditor5Field(
        'additional_info', config_name='extends', blank=True, null=True)
    additional_info_ne = CKEditor5Field(
        'additional_info_ne', config_name='extends', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/profiles/prof', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])
    order = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.name


class OfficersSpokesPerson(models.Model):
    class Meta:
        verbose_name = "Officers Spokes Person"
        verbose_name_plural = "Officers Spokes Person List"
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    additional_info = CKEditor5Field(
        'additional_info', config_name='extends', blank=True, null=True)
    additional_info_ne = CKEditor5Field(
        'additional_info_ne', config_name='extends', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/profiles/prof', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])
    order = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.name


class InformationOfficer(models.Model):
    class Meta:
        verbose_name = "Information Officer Person"
        verbose_name_plural = "Information  Officers List"
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    additional_info = CKEditor5Field(
        'additional_info', config_name='extends', blank=True, null=True)
    additional_info_ne = CKEditor5Field(
        'additional_info_ne', config_name='extends', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/profiles/prof', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])
    order = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.name
