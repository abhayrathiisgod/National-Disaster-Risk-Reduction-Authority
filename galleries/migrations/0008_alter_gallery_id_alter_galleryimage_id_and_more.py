# Generated by Django 5.0.4 on 2024-05-14 03:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("galleries", "0007_alter_galleryimage_caption_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gallery",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="galleryimage",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="videogallery",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
