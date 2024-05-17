# signals.py
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.core.files.storage import default_storage
import string
import random
import os
import fitz
from .models import NewsInfo, PressNote
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


@receiver(pre_delete, sender=NewsInfo)
def news_info_pre_delete(sender, instance, **kwargs):
    if instance.image and instance.image.name:
        if instance.image.storage == default_storage:
            try:
                default_storage.delete(instance.image.name)
            except FileNotFoundError:
                pass


@receiver(pre_delete, sender=PressNote)
def press_note_pre_delete(sender, instance, **kwargs):
    if instance.image and instance.image.name:
        if instance.image.storage == default_storage:
            try:
                default_storage.delete(instance.image.name)
            except FileNotFoundError:
                pass
    if instance.file and instance.file.name:
        if instance.file.storage == default_storage:
            try:
                default_storage.delete(instance.pdffile.name)
            except FileNotFoundError:
                pass


@receiver(pre_save, sender=NewsInfo)
def news_info_pre_save(sender, instance, **kwargs):
    if not instance.slug or NewsInfo.objects.filter(slug=instance.slug).exists():
        instance.slug = instance.generate_unique_slug()
    if instance.pk:
        old_instance = PressNote.objects.get(pk=instance.pk)
        if instance.image != old_instance.image:
            old_instance.image.delete(save=False)


@receiver(pre_save, sender=PressNote)
def press_note_pre_save(sender, instance, **kwargs):
    if not instance.slug or PressNote.objects.filter(slug=instance.slug).exists():
        instance.slug = generate_unique_slug(instance.title)

    if instance.pk:
        old_instance = PressNote.objects.get(pk=instance.pk)
        if instance.image != old_instance.image:
            old_instance.image.delete(save=False)
        if instance.file != old_instance.file:
            old_instance.file.delete(save=False)

    if instance.file:
        _, extension = os.path.splitext(instance.file.name)
        if extension.lower() == '.pdf':
            instance.file.save(
                f"{instance.title}.pdf", instance.file, save=False)

            with fitz.open(instance.file.path) as pdf:
                if pdf.page_count > 0:
                    first_page = pdf.load_page(0)
                    pix = first_page.get_pixmap()
                    img_data = pix.tobytes("jpeg")
                    img_io = BytesIO(img_data)
                    img_io.seek(0)
                    img_file = InMemoryUploadedFile(
                        img_io, None, 'first_page.jpg', 'image/jpeg', img_io.tell(), None)
                    instance.image.save('first_page.jpg', img_file, save=False)


def generate_unique_slug(title):
    slug = slugify(title)
    model = NewsInfo if isinstance(title, NewsInfo) else PressNote
    if model.objects.filter(slug=slug).exists():
        random_chars = ''.join(random.choices(
            string.ascii_letters + string.digits, k=4))
        slug += f"-{random_chars}"
    return slug
