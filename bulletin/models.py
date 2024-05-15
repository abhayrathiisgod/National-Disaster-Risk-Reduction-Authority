from django.db import models
import os
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.safestring import mark_safe


class BulletinAuthor(models.Model):
    author = models.CharField(max_length=255)
    author_ne = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.author


class BulletinType(models.Model):
    bulletin_type = models.CharField(max_length=255)
    bulletin_type_ne = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.bulletin_type


def get_upload_path_bulletin(instance, filename):
    return os.path.join('uploads/bulletin', instance.title, filename)


class Bulletin(models.Model):
    bulletin_author = models.ForeignKey(
        BulletinAuthor, on_delete=models.PROTECT)
    bulletin_type = models.ForeignKey(
        BulletinType, on_delete=models.PROTECT)
    title = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    title_ne = CKEditor5Field('Text', config_name='extends')
    summary = CKEditor5Field('Text', config_name='extends')
    summary_ne = CKEditor5Field('Text', config_name='extends')
    date = models.DateField(auto_now_add=True)
    description = CKEditor5Field('Text', config_name='extends')
    description_ne = CKEditor5Field('Text', config_name='extends')
    file = models.FileField(upload_to='uploads/bulletin/files/',
                            validators=[FileExtensionValidator(allowed_extensions=["pdf"])])
    image = models.ImageField(upload_to='uploads/bulletin/files/', validators=[
                              FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                                         "png"])])

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        self.file.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):

        if self.pk:
            old_instance = Bulletin.objects.get(pk=self.pk)
            if self.image != old_instance.image:
                old_instance.image.delete(save=False)
            if self.file != old_instance.file:
                old_instance.file.delete(save=False)
        # ra
        self.slug = slugify(self.title)
        super(Bulletin, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="250" height="250" />'.format(self.image.url))
        else:
            return '(No image)'
