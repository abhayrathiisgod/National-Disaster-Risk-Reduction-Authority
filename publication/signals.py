from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from publication.models import Publications
import os
from django.core.files.storage import default_storage
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import fitz


@receiver(pre_delete, sender=Publications)
def delete_publication_files(sender, instance, **kwargs):
    if instance.image and instance.image.name:
        if instance.image.storage == default_storage:
            try:
                default_storage.delete(instance.image.name)
            except FileNotFoundError:
                pass
    if instance.pdffile and instance.pdffile.name:
        if instance.pdffile.storage == default_storage:
            try:
                default_storage.delete(instance.pdffile.name)
            except FileNotFoundError:
                pass


@receiver(pre_save, sender=Publications)
def update_publication_files(sender, instance, **kwargs):
    if not instance.slug or Publications.objects.filter(slug=instance.slug).exists():
        instance.slug = instance.generate_unique_slug()

    if instance.pk:
        old_instance = Publications.objects.get(pk=instance.pk)
        if instance.image != old_instance.image:
            old_instance.image.delete(save=False)
        if instance.pdffile != old_instance.pdffile:
            old_instance.pdffile.delete(save=False)

    if instance.pdffile:
        _, extension = os.path.splitext(instance.pdffile.name)
        if extension.lower() == '.pdf':

            instance.pdffile.save(
                f"{instance.title}.pdf", instance.pdffile, save=False)

            with fitz.open(instance.pdffile.path) as pdf:
                if pdf.page_count > 0:
                    first_page = pdf.load_page(0)
                    pix = first_page.get_pixmap()
                    img_data = pix.tobytes("jpeg")

                    img_io = BytesIO(img_data)
                    img_io.seek(0)
                    img_file = InMemoryUploadedFile(
                        img_io, None, 'first_page.jpg', 'image/jpeg', img_io.tell(), None)
                    instance.image.save('first_page.jpg', img_file, save=False)
