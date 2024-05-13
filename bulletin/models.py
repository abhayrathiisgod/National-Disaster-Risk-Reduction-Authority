from django.db import models
import os
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
# Create your models here.


class BulletinAuthor(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=255)
    author_ne = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.author


class BulletinType(models.Model):
    id = models.AutoField(primary_key=True)
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
    title_ne = models.TextField()
    summary = models.TextField()
    summary_ne = models.TextField()
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    description_ne = models.TextField()
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
        self.slug = slugify(self.title)
        super(Bulletin, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
