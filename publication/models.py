from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from django_ckeditor_5.fields import CKEditor5Field
import random
import string


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
    pub_author = models.ForeignKey(
        PublicationAuthor, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    title_ne = models.CharField(max_length=255)
    description = CKEditor5Field(
        'Description', config_name='extends', default=' ')
    description_ne = CKEditor5Field(
        'Description_ne', config_name='extends', default=' ')
    summary = CKEditor5Field('Summary', config_name='extends', default=' ')
    summary_ne = CKEditor5Field(
        'Summary_ne', config_name='extends', default=' ')
    date = models.DateField(default='')
    pdffile = models.FileField(
        upload_to='uploads/publication/pdf', default=None, validators=[
            FileExtensionValidator(allowed_extensions=["pdf"])], blank=True, null=True)
    image = models.ImageField(upload_to='uploads/publication/image', validators=[
        FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])], blank=True, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def generate_unique_slug(self):
        slug = slugify(self.title)
        if Publications.objects.filter(slug=slug).exists():
            random_chars = ''.join(random.choices(
                string.ascii_letters + string.digits, k=4))
            slug += f"-{random_chars}"
        return slug
