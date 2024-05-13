# Generated by Django 5.0.4 on 2024-05-13 04:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bulletin", "0005_alter_bulletintype_bulletin_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bulletin",
            name="image",
            field=models.ImageField(
                upload_to="uploads/bulletin/files/",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["jpg", "jpeg", "png"]
                    )
                ],
            ),
        ),
    ]
