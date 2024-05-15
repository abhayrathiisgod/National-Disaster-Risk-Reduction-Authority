from django.db import models
import os
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from pdf2image import convert_from_path
from django.utils.safestring import mark_safe
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import random
import string
import fitz


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
    title_ne = models.TextField()
    summary = CKEditor5Field('Summary', config_name='extends')
    summary_ne = CKEditor5Field('Summary_ne', config_name='extends')
    date = models.DateField(auto_now_add=True)
    description = CKEditor5Field('Description', config_name='extends')
    description_ne = CKEditor5Field('Description_ne', config_name='extends')
    file = models.FileField(upload_to='uploads/bulletin/files/',
                            validators=[FileExtensionValidator(allowed_extensions=["pdf"])])
    image = models.ImageField(upload_to='uploads/bulletin/files/', validators=[
                              FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                                         "png"])], blank=True, null=True)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        self.file.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if not self.slug or Bulletin.objects.filter(slug=self.slug).exists():
            self.slug = self.generate_unique_slug()
        if self.pk:
            old_instance = Bulletin.objects.get(pk=self.pk)
            if self.image != old_instance.image:
                old_instance.image.delete(save=False)
            if self.file != old_instance.file:
                old_instance.file.delete(save=False)
        super().save(*args, **kwargs)
        if self.file:
            _, extension = os.path.splitext(self.file.name)
            self.file_extension = extension
            if extension.lower() == '.pdf':
                image_data = self.extract_first_page_as_image()
                if image_data:
                    self.image.save('first_page.jpg', image_data, save=False)
        super(Bulletin, self).save(*args, **kwargs)

    def generate_unique_slug(self):
        slug = slugify(self.title)
        if Bulletin.objects.filter(slug=slug).exists():
            random_chars = ''.join(random.choices(
                string.ascii_letters + string.digits, k=4))
            slug += f"-{random_chars}"
        return slug

    def extract_first_page_as_image(self):
        if self.file:
            images = convert_from_path(self.file.path)
            if images:
                first_page_image = images[0]

                img_io = BytesIO()
                first_page_image.save(img_io, format='JPEG')
                img_io.seek(0)

                img_file = InMemoryUploadedFile(
                    img_io, None, 'first_page.jpg', 'image/jpeg', img_io.tell(), None)

                return img_file

        return None

    def __str__(self) -> str:
        return self.title

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="250" height="250" />'.format(self.image.url))
        else:
            return '(No image)'
