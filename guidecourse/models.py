from django.db import models

# Create your models here.


class GuideCourse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    description = models.TextField()
    description_ne = models.TextField()
    image = models.ImageField(upload_to='uploads/guide_course')

    def __str__(self) -> str:
        return self.name


class Guidechildren(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.ManyToManyField(
        'GuideCourse', related_name='children', blank=True)
    name = models.CharField(max_length=255)
    name_ne = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    description = models.TextField()
    description_ne = models.TextField()
    image = models.ImageField(
        upload_to='uploads/guide_course/children/', default=None, null=True)

    def __str__(self) -> str:
        return self.name


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    path = models.URLField()
    image = models.ImageField(upload_to='uploads/guide_course/course')
    youtube_url = models.URLField()
    description = models.TextField()
    description_ne = models.TextField()
    target_audience = models.TextField()
    target_audience_ne = models.TextField()
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
    learning_objective = models.TextField()
    learning_objective_ne = models.TextField()

    def __str__(self):
        return self.title
