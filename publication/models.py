from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from PyPDF2 import PdfFileReader
from pdf2image import convert_from_path
from io import BytesIO
from django.conf import settings
from django_ckeditor_5.fields import CKEditor5Field
from django.core.files.uploadedfile import InMemoryUploadedFile
import os
from django.utils.safestring import mark_safe


class PublicationType(models.Model):
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
    publication_author = models.CharField(
        max_length=255, default='National Disaster Risk Reduction and Management Authority')
    publication_author_ne = models.CharField(
        max_length=255, default='राष्ट्रिय विपद् जोखिम न्यूनीकरण तथा व्यवस्थापन प्राधिकरण')

    def __str__(self) -> str:
        return self.publication_author


class Publications(models.Model):
    pub_type = models.ForeignKey(PublicationType, on_delete=models.PROTECT)
    pub_author = models.ForeignKey(PublicationAuthor, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    title_ne = models.CharField(max_length=255)
    description = CKEditor5Field('Text', config_name='extends', default=' ')
    description_ne = CKEditor5Field('Text', config_name='extends', default=' ')
    summary = CKEditor5Field('Text', config_name='extends', default=' ')
    summary_ne = CKEditor5Field('Text', config_name='extends', default=' ')
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
        super().save(*args, **kwargs)
        if self.pdffile:
            _, extension = os.path.splitext(self.pdffile.name)
            self.file_extension = extension
            if extension.lower() == '.pdf':
                image_data = self.extract_first_page_as_image()
                if image_data:
                    self.image.save('first_page.jpg', image_data, save=False)
        self.slug = slugify(self.title)
        if self.pk:
            old_instance = Publications.objects.get(pk=self.pk)
            if self.image != old_instance.image:
                old_instance.image.delete(save=False)
            if self.pdffile != old_instance.pdffile:
                old_instance.pdffile.delete(save=False)

        super(Publications, self).save(*args, **kwargs)

    def extract_first_page_as_image(self):
        if self.pdffile:
            images = convert_from_path(self.pdffile.path)
            if images:
                first_page_image = images[0]

                img_io = BytesIO()
                first_page_image.save(img_io, format='JPEG')
                img_io.seek(0)

                img_file = InMemoryUploadedFile(
                    img_io, None, 'first_page.jpg', 'image/jpeg', img_io.tell(), None)

                return img_file

        return None

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="250" height="250" />'.format(self.image.url))
        else:
            return '(No image)'
