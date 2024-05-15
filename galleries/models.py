from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.safestring import mark_safe
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Gallery(models.Model):
    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/gallery/display_image/')

    def __str__(self):
        return self.title

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="250" height="250" />'.format(self.image.url))
        else:
            return '(No image)'


class GalleryImage(models.Model):
    class Meta:
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"
    gallery = models.ForeignKey(
        Gallery, on_delete=models.PROTECT, related_name='images')
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

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="150" height="150" />'.format(self.image.url))
        else:
            return '(No image)'


class VideoGallery(models.Model):
    class Meta:
        verbose_name = "Video Gallery"
        verbose_name_plural = "Video Galleries"
    youtube_url = models.URLField()

    def __str__(self) -> str:
        return str(self.id)


# signalss


@receiver(pre_delete, sender=GalleryImage)
def delete_gallery_image_file(sender, instance, **kwargs):
    # Delete the associated image file when a GalleryImage instance is deleted
    instance.image.delete(save=False)
