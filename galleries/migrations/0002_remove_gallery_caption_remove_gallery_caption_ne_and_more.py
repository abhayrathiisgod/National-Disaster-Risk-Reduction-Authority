# Generated by Django 5.0.4 on 2024-04-29 08:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("galleries", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="gallery",
            name="caption",
        ),
        migrations.RemoveField(
            model_name="gallery",
            name="caption_ne",
        ),
        migrations.RemoveField(
            model_name="gallery",
            name="photo_credit",
        ),
        migrations.RemoveField(
            model_name="gallery",
            name="photo_credit_ne",
        ),
        migrations.AlterField(
            model_name="gallery",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="gallery",
            name="image",
            field=models.URLField(),
        ),
        migrations.CreateModel(
            name="GalleryImage",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                ("title_ne", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "photo_credit",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "photo_credit_ne",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("caption", models.TextField(blank=True, null=True)),
                ("caption_ne", models.TextField(blank=True, null=True)),
                ("image", models.URLField()),
                (
                    "gallery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="galleries.gallery",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="DisplayImage",
        ),
    ]