# Generated by Django 5.0.4 on 2024-04-29 08:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("galleries", "0002_remove_gallery_caption_remove_gallery_caption_ne_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="galleryimage",
            name="image",
            field=models.ImageField(upload_to="uploads/gallery/"),
        ),
    ]
