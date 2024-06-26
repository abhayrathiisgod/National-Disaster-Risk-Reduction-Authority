# Generated by Django 5.0.4 on 2024-05-13 06:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("publication", "0005_alter_publications_pub_author_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publications",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="uploads/publication/image",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["jpg", "jpeg", "png"]
                    )
                ],
            ),
        ),
    ]
