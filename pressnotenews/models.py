from django.db import models
from django.core.validators import FileExtensionValidator
from django_ckeditor_5.fields import CKEditor5Field


class Author(models.Model):

    Author_id = models.AutoField(primary_key=True)
    name = models.CharField()
    name_ne = models.CharField()

    def __str__(self) -> str:
        return self.name


class Type(models.Model):

    Type_id = models.AutoField(primary_key=True)
    name = models.CharField()
    name_ne = models.CharField()

    def __str__(self) -> str:
        return self.name


class NewsInfo(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = CKEditor5Field('Description', config_name='extends')
    description_ne = CKEditor5Field('Description_ne', config_name='extends')
    summary = CKEditor5Field('Summary', config_name='extends')
    summary_ne = CKEditor5Field('Summary_ne', config_name='extends')
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/news_info', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])

    def __str__(self) -> str:
        return self.title


class PressNote(models.Model):

    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)
    type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = CKEditor5Field('Text', config_name='extends')
    description_ne = CKEditor5Field('Text', config_name='extends')
    summary = CKEditor5Field('Text', config_name='extends')
    summary_ne = CKEditor5Field('Text', config_name='extends')
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/press-note', blank=True, null=True, validators=[
        FileExtensionValidator(allowed_extensions=["pdf", "doc",
                                                   "docx"])])
    image = models.ImageField(upload_to='uploads/files/press-note', blank=True, null=True, validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])])
    is_published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
