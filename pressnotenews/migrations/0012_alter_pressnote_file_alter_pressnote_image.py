# Generated by Django 5.0.4 on 2024-05-17 04:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pressnotenews", "0011_alter_pressnote_image_alter_pressnote_title_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pressnote",
            name="file",
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
            name="image",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="uploads/files/press-note",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["jpg", "jpeg", "png"]
                    )
                ],
            ),
        ),
    ]
