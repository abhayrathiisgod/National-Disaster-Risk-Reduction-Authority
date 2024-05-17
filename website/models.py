from django.db import models
from publication.models import Publications
from django.core.validators import FileExtensionValidator
from django_ckeditor_5.fields import CKEditor5Field
from django.db import models


class ContactDetail(models.Model):
    class Meta:
        verbose_name = "Contact Detail"
        verbose_name_plural = "Contact Detail List"
    detail = CKEditor5Field('Detail', config_name='extends')
    detail_ne = CKEditor5Field('Detail_ne', config_name='extends')

    def __str__(self) -> str:
        return self.detail


class Introduction(models.Model):
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    description = CKEditor5Field('description_ne', config_name='extends')
    description_ne = CKEditor5Field('description_ne', config_name='extends')
    sub_title = CKEditor5Field('subtitle', config_name='extends')
    sub_title_ne = CKEditor5Field('subtitle_ne', config_name='extends')
    content = CKEditor5Field('content', config_name='extends')
    content_ne = CKEditor5Field('content_ne', config_name='extends')

    def __str__(self) -> str:
        return self.title


class WardDocument(models.Model):
    filename = models.CharField(max_length=255)
    filename_ne = models.CharField(max_length=255)
    document = models.FileField(upload_to='uploads/ward_document')
    file_extension = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='uploads/ward_document_images', blank=True, null=True)

    def __str__(self):
        return self.filename


class FrequentlyAskedQuestions(models.Model):
    class Meta:
        verbose_name = "Frequently Asked Question"
        verbose_name_plural = "Frequently Asked Questions"
    question = CKEditor5Field('question', config_name='extends')
    question_ne = CKEditor5Field('question_ne', config_name='extends')
    answer = CKEditor5Field('answer', config_name='extends')
    answer_ne = CKEditor5Field('answer_ne', config_name='extends')

    def __str__(self) -> str:
        return self.question


class Page(models.Model):
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    featured_image = models.ImageField(
        upload_to='uploads/page/featured_image', null=True, blank=True, validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                       "png"])])
    description = CKEditor5Field('description', config_name='extends')
    description_ne = CKEditor5Field('description_ne', config_name='extends')
    slug = models.SlugField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title


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


class NdrmaPortals(models.Model):
    class Meta:
        verbose_name = "Ndrma Portal"
        verbose_name_plural = "Ndrma Portals List"

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='ndrmaPortal/icons/')
    realted_link = models.URLField()

    def __str__(self):
        return self.name
