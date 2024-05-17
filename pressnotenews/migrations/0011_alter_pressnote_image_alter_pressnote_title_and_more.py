# Generated by Django 5.0.4 on 2024-05-17 04:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pressnotenews", "0010_alter_newsinfo_title_alter_newsinfo_title_ne"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pressnote",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="uploads/press-note",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["pdf", "doc", "docx"]
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="pressnote",
            name="title",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="pressnote",
            name="title_ne",
            field=models.CharField(max_length=255),
        ),
    ]
