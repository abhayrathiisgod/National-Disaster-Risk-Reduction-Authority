from django.db.models.signals import post_save
from django.dispatch import receiver
from publication.models import Publications
from PyPDF2 import PdfFileReader
from pdf2image import convert_from_path
import os


@receiver(post_save, sender=Publications)
def generate_image(sender, instance, created, **kwargs):
    if created:
        pdf_path = instance.pdffile.path
        pages = convert_from_path(pdf_path, 300)
        first_page_image = pages[0]
        instance.image.save(os.path.basename(
            pdf_path) + '_first_page.jpg', first_page_image, save=True)
