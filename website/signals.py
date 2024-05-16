from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from .models import NdrmaPortals, HomePageBanner, Page, WardDocument
from pdf2image import convert_from_path
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import os


@receiver(pre_save, sender=WardDocument)
def delete_old_document_image(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = WardDocument.objects.get(pk=instance.pk)
            if instance.document != old_instance.document:
                old_instance.document.delete(save=False)
                if old_instance.image:
                    old_instance.image.delete(save=False)
        except WardDocument.DoesNotExist:
            pass

    if instance.document:
        _, extension = os.path.splitext(instance.document.name)
        if extension.lower() == '.pdf':

            instance.document.save(
                f"{instance.filename}.pdf", instance.document, save=False)

            images = convert_from_path(instance.document.path)
            if images:
                first_page_image = images[0]
                img_io = BytesIO()
                first_page_image.save(img_io, format='JPEG')
                img_io.seek(0)
                img_file = InMemoryUploadedFile(
                    img_io, None, 'first_page.jpg', 'image/jpeg', img_io.tell(), None)
                instance.image.save('first_page.jpg', img_file, save=False)


@receiver(pre_delete, sender=WardDocument)
def delete_document_image(sender, instance, **kwargs):
    if instance.document:
        instance.document.delete(save=False)
    if instance.image:
        instance.image.delete(save=False)


@receiver(pre_save, sender=Page)
def delete_old_featured_image(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = Page.objects.get(pk=instance.pk)
            if instance.featured_image != old_instance.featured_image:
                old_instance.featured_image.delete(save=False)
        except Page.DoesNotExist:
            pass


@receiver(pre_delete, sender=Page)
def delete_featured_image(sender, instance, **kwargs):
    if instance.featured_image:
        instance.featured_image.delete(save=False)


@receiver(pre_save, sender=NdrmaPortals)
def delete_old_image(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = NdrmaPortals.objects.get(pk=instance.pk)
            if instance.image != old_instance.image:
                old_instance.image.delete(save=False)
        except NdrmaPortals.DoesNotExist:
            pass


@receiver(pre_delete, sender=NdrmaPortals)
def delete_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)


@receiver(pre_save, sender=HomePageBanner)
def delete_old_image(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = HomePageBanner.objects.get(pk=instance.pk)
            if instance.image != old_instance.image:
                old_instance.image.delete(save=False)
        except HomePageBanner.DoesNotExist:
            pass


@receiver(pre_delete, sender=HomePageBanner)
def delete_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)
