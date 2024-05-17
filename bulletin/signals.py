from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Bulletin
import os
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import fitz

# Define a flag to avoid recursion
processing_instance = set()


@receiver(pre_save, sender=Bulletin)
def pre_save_bulletin(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
    if Bulletin.objects.filter(slug=instance.slug).exists():
        instance.slug = instance.generate_unique_slug()

    if instance.pk:
        old_instance = Bulletin.objects.get(pk=instance.pk)
        if instance.image != old_instance.image:
            old_instance.image.delete(save=False)
        if instance.file != old_instance.file:
            old_instance.file.delete(save=False)


@receiver(post_save, sender=Bulletin)
def post_save_bulletin(sender, instance, **kwargs):
    if instance.pk in processing_instance:
        return

    processing_instance.add(instance.pk)

    if instance.file:
        _, extension = os.path.splitext(instance.file.name)
        if extension.lower() == '.pdf':
            # Save the PDF file first
            instance.file.save(f"{instance.title}.pdf",
                               instance.file, save=False)

            # Convert the first page of the PDF to an image
            image_data = instance.extract_first_page_as_image()
            if image_data:
                instance.image.save('first_page.jpg', image_data, save=False)
                # Use update_fields to avoid triggering another save
                Bulletin.objects.filter(pk=instance.pk).update(
                    image=instance.image)

    processing_instance.remove(instance.pk)


@receiver(post_delete, sender=Bulletin)
def post_delete_bulletin(sender, instance, **kwargs):
    instance.image.delete(save=False)
    instance.file.delete(save=False)
