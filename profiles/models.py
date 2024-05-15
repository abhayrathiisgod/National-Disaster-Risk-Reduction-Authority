from django.db import models
from django.core.validators import FileExtensionValidator
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.safestring import mark_safe
# Create your models here.


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
    description = CKEditor5Field('Text', config_name='extends')
    description_ne = CKEditor5Field('Text', config_name='extends')
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
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    additional_info = CKEditor5Field('Text', config_name='extends')
    additional_info_ne = CKEditor5Field('Text', config_name='extends')
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

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="250" height="250" />'.format(self.image.url))
        else:
            return '(No image)'


class CommiteProfile(models.Model):
    class Meta:
        verbose_name = "Committee Profile"
        verbose_name_plural = "Committee Profilee List"
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    additional_info = CKEditor5Field(
        'Text', config_name='extends', blank=True, null=True)
    additional_info_ne = CKEditor5Field(
        'Text', config_name='extends', blank=True, null=True)
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

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="250" height="250" />'.format(self.image.url))
        else:
            return '(No image)'


class NationalCouncilHead(models.Model):
    class Meta:
        verbose_name = "National Council Head"
        verbose_name_plural = "National Council Head List"
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    additional_info = CKEditor5Field(
        'Text', config_name='extends', blank=True, null=True)
    additional_info_ne = CKEditor5Field(
        'Text', config_name='extends', blank=True, null=True)
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

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="250" height="250" />'.format(self.image.url))
        else:
            return '(No image)'


class ExecutiveCommitteHead(models.Model):
    class Meta:
        verbose_name = "Executive Committee Head"
        verbose_name_plural = "Executive Committee Head List"
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    additional_info = CKEditor5Field(
        'Text', config_name='extends', blank=True, null=True)
    additional_info_ne = CKEditor5Field(
        'Text', config_name='extends', blank=True, null=True)
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

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="250" height="250" />'.format(self.image.url))
        else:
            return '(No image)'


class OfficersHead(models.Model):
    class Meta:
        verbose_name = "Officers Head"
        verbose_name_plural = "Officers Head List"
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    additional_info = CKEditor5Field(
        'Text', config_name='extends', blank=True, null=True)
    additional_info_ne = CKEditor5Field(
        'Text', config_name='extends', blank=True, null=True)
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

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="250" height="250" />'.format(self.image.url))
        else:
            return '(No image)'


class OfficersSpokesPerson(models.Model):
    class Meta:
        verbose_name = "Officers Spokes Person"
        verbose_name_plural = "Officers Spokes Person List"
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    additional_info = CKEditor5Field(
        'Text', config_name='extends', blank=True, null=True)
    additional_info_ne = CKEditor5Field(
        'Text', config_name='extends', blank=True, null=True)
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

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="250" height="250" />'.format(self.image.url))
        else:
            return '(No image)'


class InformationOfficer(models.Model):
    class Meta:
        verbose_name = "Information Officer Person"
        verbose_name_plural = "Information Officers List"
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    name_ne = models.CharField(max_length=100)
    additional_info = CKEditor5Field(
        'Text', config_name='extends', blank=True, null=True)
    additional_info_ne = CKEditor5Field(
        'Text', config_name='extends', blank=True, null=True)
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

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="250" height="250" />'.format(self.image.url))
        else:
            return '(No image)'
