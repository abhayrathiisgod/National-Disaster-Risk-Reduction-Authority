from django.db import models
import os


class ContactDetail(models.Model):
    id = models.AutoField(primary_key=True)
    detail = models.TextField()
    detail_ne = models.TextField()


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
