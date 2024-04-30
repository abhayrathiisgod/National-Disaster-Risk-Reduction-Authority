from django.db import models

# Create your models here.


class Hazards(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    title_ne = models.CharField(max_length=255)
    order = models.IntegerField()
    description = models.TextField()
    icon = models.ImageField(upload_to='hazard_icons/')
    color = models.CharField(max_length=255)
    hazard_type = (
        ('Natural', 'Natural'),
        ('Non-Natural', 'Non-Natural'),
    )
    type = models.CharField(max_length=255, choices=hazard_type)

    def __str__(self) -> str:
        return self.title
