from django.db import models

# Create your models here.


class GuideCourse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    description = models.TextField()
    description_ne = models.TextField()
    image = models.ImageField(upload_to='uploads/guide_course')


class Guidechildren(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    name_ne = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    description = models.TextField()
    description_ne = models.TextField()
    parent = models.ForeignKey(GuideCourse, on_delete=models.CASCADE)
