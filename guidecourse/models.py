from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.safestring import mark_safe
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class GuideCourse(models.Model):
    class Meta:
        verbose_name = "Guide"
        verbose_name_plural = "Guides"
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    description = CKEditor5Field(
        'description', config_name='extends', blank=True, null=True)
    description_ne = CKEditor5Field(
        'description_ne', config_name='extends', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/guide_course')

    def __str__(self) -> str:
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):

        if self.pk:
            old_instance = GuideCourse.objects.get(pk=self.pk)
            if self.image != old_instance.image:
                old_instance.image.delete(save=False)

        super(GuideCourse, self).save(*args, **kwargs)


class Guidechildren(models.Model):
    class Meta:
        verbose_name = "Guide Children"
        verbose_name_plural = "Guide Childrens"
    parent = models.ManyToManyField(
        'GuideCourse', related_name='children', blank=True)
    name = models.CharField(max_length=255)
    name_ne = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    description = CKEditor5Field(
        'Description', config_name='extends', blank=True, null=True)
    description_ne = CKEditor5Field(
        'Description_ne', config_name='extends', blank=True, null=True)
    image = models.ImageField(
        upload_to='uploads/guide_course/children/', default=None, null=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):

        if self.pk:
            old_instance = Guidechildren.objects.get(pk=self.pk)
            if self.image != old_instance.image:
                old_instance.image.delete(save=False)

        super(Guidechildren, self).save(*args, **kwargs)


class Course(models.Model):
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    path = models.URLField()
    image = models.ImageField(upload_to='uploads/guide_course/course')
    youtube_url = models.URLField()
    description = CKEditor5Field(
        'Description', config_name='extends', blank=True, null=True)
    description_ne = CKEditor5Field(
        'Description_ne', config_name='extends', blank=True, null=True)
    target_audience = CKEditor5Field(
        'Target_audience', config_name='extends', blank=True, null=True)
    target_audience_ne = CKEditor5Field(
        'Target_audience_ne', config_name='extends', blank=True, null=True)
    duration = models.CharField(max_length=55)
    SKILL_LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    skill_level = models.CharField(max_length=20, choices=SKILL_LEVEL_CHOICES)
    LANGUAGE_CHOICES = [
        ('English', 'English'),
        ('Nepali', 'Nepali'),
    ]
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    learning_objective = CKEditor5Field(
        'learning_objective', config_name='extends', blank=True, null=True)
    learning_objective_ne = CKEditor5Field(
        'learning_objective_ne', config_name='extends', blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if self.pk:
            old_instance = Course.objects.get(pk=self.pk)
            if self.image != old_instance.image:
                old_instance.image.delete(save=False)

        super(Course, self).save(*args, **kwargs)


@receiver(pre_delete, sender=GuideCourse)
def guide_course_image_file(sender, instance, **kwargs):
    instance.image.delete(save=False)


@receiver(pre_delete, sender=Course)
def course_image_file(sender, instance, **kwargs):
    instance.image.delete(save=False)
