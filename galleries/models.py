from django.db import models


class Gallery(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/gallery/display_image/')

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    gallery = models.ForeignKey(
        Gallery, on_delete=models.PROTECT, related_name='images')
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    title_ne = models.CharField(max_length=255, blank=True, null=True)
    photo_credit = models.CharField(max_length=255, blank=True, null=True)
    photo_credit_ne = models.CharField(max_length=255, blank=True, null=True)
    caption = models.TextField(blank=True, null=True)
    caption_ne = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/gallery/')

    def __str__(self):
        return f"Image {self.id} of {self.gallery.title}"

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):

        if self.pk:
            old_instance = GalleryImage.objects.get(pk=self.pk)
            if self.image != old_instance.image:
                old_instance.image.delete(save=False)

        super(GalleryImage, self).save(*args, **kwargs)


class VideoGallery(models.Model):
    id = models.IntegerField(primary_key=True)
    youtube_url = models.URLField()

    def __str__(self) -> str:
        return self.id
