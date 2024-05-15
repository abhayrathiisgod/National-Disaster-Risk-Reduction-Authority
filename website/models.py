from django.db import models
from publication.models import Publications
import os
from django.core.validators import FileExtensionValidator
from django_ckeditor_5.fields import CKEditor5Field
from pdf2image import convert_from_path
from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.safestring import mark_safe


class ContactDetail(models.Model):
    class Meta:
        verbose_name = "Contact Detail"
        verbose_name_plural = "Contact Detail List"
    detail = CKEditor5Field('Text', config_name='extends')
    detail_ne = CKEditor5Field('Text', config_name='extends')

    def __str__(self) -> str:
        return self.detail


class Introduction(models.Model):
    title = CKEditor5Field('Text', config_name='extends')
    title_ne = CKEditor5Field('Text', config_name='extends')
    description = CKEditor5Field('Text', config_name='extends')
    description_ne = CKEditor5Field('Text', config_name='extends')
    sub_title = CKEditor5Field('Text', config_name='extends')
    sub_title_ne = CKEditor5Field('Text', config_name='extends')
    content = CKEditor5Field('Text', config_name='extends')
    content_ne = CKEditor5Field('Text', config_name='extends')

    def __str__(self) -> str:
        return self.title


class WardDocument(models.Model):
    filename = models.CharField(max_length=255)
    filename_ne = models.CharField(max_length=255)
    document = models.FileField(upload_to='uploads/ward_document')
    file_extension = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='uploads/ward_document_images', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.document:
            _, extension = os.path.splitext(self.document.name)
            self.file_extension = extension
            if extension.lower() == '.pdf':
                image_data = self.extract_first_page_as_image()
                if image_data:
                    self.image.save('first_page.jpg', image_data, save=False)

        super().save(*args, **kwargs)

    def extract_first_page_as_image(self):
        if self.document:
            images = convert_from_path(self.document.path)
            if images:
                first_page_image = images[0]

                img_io = BytesIO()
                first_page_image.save(img_io, format='JPEG')
                img_io.seek(0)

                img_file = InMemoryUploadedFile(
                    img_io, None, 'first_page.jpg', 'image/jpeg', img_io.tell(), None)

                return img_file

        return None

    def __str__(self):
        return self.filename

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete(save=False)
        self.document.delete(save=False)
        super().delete(*args, **kwargs)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="250" height="250" />'.format(self.image.url))
        else:
            return '(No image)'


class FrequentlyAskedQuestions(models.Model):
    class Meta:
        verbose_name = "Frequently Asked Question"
        verbose_name_plural = "Frequently Asked Questions"
    question = CKEditor5Field('Text', config_name='extends')
    question_ne = CKEditor5Field('Text', config_name='extends')
    answer = CKEditor5Field('Text', config_name='extends')
    answer_ne = CKEditor5Field('Text', config_name='extends')

    def __str__(self) -> str:
        return self.question


class Page(models.Model):
    title = CKEditor5Field('Text', config_name='extends')
    title_ne = CKEditor5Field('Text', config_name='extends')
    featured_image = models.ImageField(
        upload_to='uploads/page/featured_image', null=True, blank=True, validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                       "png"])])
    description = CKEditor5Field('Text', config_name='extends')
    description_ne = CKEditor5Field('Text', config_name='extends')
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.title

    def delete(self, *args, **kwargs):
        self.featured_image.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = Page.objects.get(pk=self.pk)
            if self.featured_image != old_instance.featured_image:
                old_instance.featured_image.delete(save=False)

        super(Page, self).save(*args, **kwargs)


class Bookmarks(models.Model):
    class Meta:
        verbose_name = "Bookmark"
        verbose_name_plural = "Bookmarks"
    name = models.TextField()
    name_ne = models.TextField()
    link = models.URLField()

    def __str__(self) -> str:
        return self.name


class Menu(models.Model):
    name = models.TextField()
    name_ne = models.TextField()
    parent = models.ForeignKey(
        'self', on_delete=models.PROTECT, related_name='children', null=True, blank=True)

    link = models.CharField(max_length=100, null=True, blank=True)
    is_external_link = models.BooleanField(default=False)
    content_source = models.ForeignKey(
        Publications, on_delete=models.PROTECT, null=True, blank=True)
    page = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class ContactForm(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.full_name


class HomePageBanner(models.Model):
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/homepage/banner', validators=[
                              FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                                         "png"])])

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = HomePageBanner.objects.get(pk=self.pk)
            if self.image != old_instance.image:
                old_instance.image.delete(save=False)

        super(HomePageBanner, self).save(*args, **kwargs)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="250" height="250" />'.format(self.image.url))
        else:
            return '(No image)'


class NdrmaPortals(models.Model):
    class Meta:
        verbose_name = "Ndrma Portal"
        verbose_name_plural = "Ndrma Portals List"

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='ndrmaPortal/icons/')
    realted_link = models.URLField()

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = HomePageBanner.objects.get(pk=self.pk)
            if self.image != old_instance.image:
                old_instance.image.delete(save=False)

        super(HomePageBanner, self).save(*args, **kwargs)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="250" height="250" />'.format(self.image.url))
        else:
            return '(No image)'
