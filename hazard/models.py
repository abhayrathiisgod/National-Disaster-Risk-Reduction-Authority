from django.db import models
from django.core.validators import FileExtensionValidator
from django_ckeditor_5.fields import CKEditor5Field


class Hazards(models.Model):
    class Meta:
        verbose_name = "Hazard"
        verbose_name_plural = "Hazards"
    title = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    order = models.IntegerField(unique=True)
    description = CKEditor5Field('Text', config_name='extends')
    icon = models.ImageField(upload_to='uplods/hazard_icons/', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])
    color = models.CharField(max_length=255)
    hazard_type = (
        ('Natural', 'Natural'),
        ('Non-Natural', 'Non-Natural'),
    )
    type = models.CharField(max_length=255, choices=hazard_type)

    def __str__(self) -> str:
        return self.title

    def delete(self, *args, **kwargs):
        self.icon.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):

        if self.pk:
            old_instance = Hazards.objects.get(pk=self.pk)
            if self.icon != old_instance.icon:
                old_instance.icon.delete(save=False)

        super(Hazards, self).save(*args, **kwargs)
