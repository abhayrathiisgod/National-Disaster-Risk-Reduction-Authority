from django.db import models
import os
# Create your models here.


class BulletinAuthor(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=255)
    author_ne = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.author


class BulletinType(models.Model):
    id = models.AutoField(primary_key=True)
    bulletin_type = models.CharField(max_length=50)
    bulletin_type_ne = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.bulletin_type


def get_upload_path_bulletin(instance, filename):
    return os.path.join('uploads/bulletin', instance.title, filename)


class Bulletin(models.Model):
    bulletin_author = models.ForeignKey(
        BulletinAuthor, on_delete=models.DO_NOTHING)
    bulletin_type = models.ForeignKey(
        BulletinType, on_delete=models.DO_NOTHING)
    title = models.TextField()
    title_ne = models.TextField()
    summary = models.TextField()
    summary_ne = models.TextField()
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    description_ne = models.TextField()
    file = models.FileField(upload_to='uploads/bulletin/files/')
    image = models.ImageField(upload_to=get_upload_path_bulletin)

    def __str__(self) -> str:
        return self.title
