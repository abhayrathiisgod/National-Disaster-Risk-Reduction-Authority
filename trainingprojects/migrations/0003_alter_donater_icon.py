# Generated by Django 5.0.4 on 2024-05-13 05:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trainingprojects", "0002_training"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donater",
            name="icon",
            field=models.ImageField(
                upload_to="uploads/donater/icon",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["jpg", "jpeg", "png"]
                    )
                ],
            ),
        ),
    ]