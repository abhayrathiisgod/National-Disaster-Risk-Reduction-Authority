# Generated by Django 5.0.4 on 2024-05-13 05:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("publication", "0003_publications_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publications",
            name="image",
            field=models.ImageField(
                upload_to="uploads/publication/image",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["jpg", "jpeg", "png"]
                    )
                ],
            ),
        ),
    ]
