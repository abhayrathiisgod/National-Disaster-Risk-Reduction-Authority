from django.db import models
from publication.models import Publications
import os


class ContactDetail(models.Model):
    id = models.AutoField(primary_key=True)
    detail = models.TextField()
    detail_ne = models.TextField()

    def __str__(self) -> str:
        return self.detail


class Introduction(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    title_ne = models.TextField()
    description = models.TextField()
    description_ne = models.TextField()
    sub_title = models.TextField()
    sub_title_ne = models.TextField()
    content = models.TextField()
    content_ne = models.TextField()

    def __str__(self) -> str:
        return self.title


class WardDocument(models.Model):
    id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=255)
    filename_ne = models.CharField(max_length=255)
    document = models.FileField(upload_to='uploads/ward_document')
    file_extension = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):

        _, extension = os.path.splitext(self.document.name)
        self.file_extension = extension
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.filename


class FrequentlyAskedQuestions(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    question_ne = models.TextField()
    answer = models.TextField()
    answer_ne = models.TextField()

    def __str__(self) -> str:
        return self.question


class Page(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    title_ne = models.TextField()
    featured_image = models.ImageField(
        upload_to='uploads/page/featured_image', null=True, blank=True)
    description = models.TextField()
    description_ne = models.TextField()
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.title


class Bookmarks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    name_ne = models.TextField()
    link = models.URLField()

    def __str__(self) -> str:
        return self.name


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    name_ne = models.TextField()
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    link = models.CharField(max_length=100, null=True, blank=True)
    is_external_link = models.BooleanField(default=False)
    content_source = models.ForeignKey(
        Publications, on_delete=models.CASCADE, null=True, blank=True)
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
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/homepage/banner')
