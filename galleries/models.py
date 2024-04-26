from django.db import models

# Create your models here.


class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    photo_credit = models.CharField(max_length=255)
    photo_credit_ne = models.CharField(max_length=255)
    caption = models.TextField()
    caption_ne = models.TextField()
    image = models.ImageField(upload_to='uploads/gallery')

# main display Image is the class below


class DisplayImage(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/display_image')
    other_images = models.ManyToManyField(Gallery)
