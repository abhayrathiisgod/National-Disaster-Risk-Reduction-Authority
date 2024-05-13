from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from PyPDF2 import PdfFileReader
from pdf2image import convert_from_path
from django.conf import settings
import os


class PublicationType(models.Model):
    id = models.AutoField(primary_key=True)
    pub_choice = (
        ('Decision/Circular/Directive', 'Decision_Circular_Directive'),
        ('Rules and Regulations', 'Rules_and_Regulations'),
        ('Policies and Directories', 'Policies_and_Directories'),
        ('Report', 'Report'),
        ('Procedure', 'Procedure'),
        ('Plan', 'Plan'),
        ('Articles', 'Articles'),
        ('Criteria', 'Criteria'),
        ('MeetingReport', 'MeetingReport'),
        ('Tender', 'Tender'),
    )
    pub_choice_ne = (
        ('निर्णय/सर्कुलर/निर्देशिका', 'निर्णय_सर्कुलर_निर्देशिका'),
        ('नियम तथा विनियम', 'नियम_तथा_विनियम'),
        ('नीति तथा दिशानिर्देशन', 'नीति_तथा_दिशानिर्देशन'),
        ('प्रतिवेदन', 'प्रतिवेदन'),
        ('प्रक्रिया', 'प्रक्रिया'),
        ('योजना', 'योजना'),
        ('लेख', 'लेख'),
        ('मापदण्ड', 'मापदण्ड'),
        ('बैठकको_प्रतिवेदन', 'बैठकको_प्रतिवेदन'),
        ('टेन्डर', 'टेन्डर'),
    )
    publication_type = models.CharField(max_length=255, choices=pub_choice)
    publication_type_ne = models.CharField(
        max_length=255, choices=pub_choice_ne)

    def __str__(self) -> str:
        return self.publication_type


class PublicationAuthor(models.Model):
    id = models.AutoField(primary_key=True)
    publication_author = models.CharField(
        max_length=255, default='National Disaster Risk Reduction and Management Authority')
    publication_author_ne = models.CharField(
        max_length=255, default='राष्ट्रिय विपद् जोखिम न्यूनीकरण तथा व्यवस्थापन प्राधिकरण')

    def __str__(self) -> str:
        return self.publication_author


class Publications(models.Model):
    id = models.AutoField(primary_key=True)
    pub_type = models.ForeignKey(PublicationType, on_delete=models.PROTECT)
    pub_author = models.ForeignKey(PublicationAuthor, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    title_ne = models.CharField(max_length=255)
    description = models.TextField(default='')
    description_ne = models.TextField(default='')
    summary = models.TextField(default='')
    summary_ne = models.TextField(default='')
    date = models.DateField(default='')
    pdffile = models.FileField(
        upload_to='uploads/publication/pdf', default=None)
    image = models.ImageField(upload_to='uploads/publication/image', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg",
                                                   "png"])], blank=True, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.pk:
            old_instance = Publications.objects.get(pk=self.pk)
            if self.image != old_instance.image:
                old_instance.image.delete(save=False)
            if self.pdffile != old_instance.pdffile:
                old_instance.pdffile.delete(save=False)

        super(Publications, self).save(*args, **kwargs)


# def convert_pdf_to_image(sender, instance, created, **kwargs):
