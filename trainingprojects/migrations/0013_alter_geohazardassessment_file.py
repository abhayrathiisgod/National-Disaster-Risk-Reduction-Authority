# Generated by Django 5.0.4 on 2024-05-17 07:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trainingprojects", "0012_fiscal_geohazardassessment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="geohazardassessment",
            name="file",
            field=models.FileField(
                blank=True, null=True, upload_to="uploads/geohazardassessment/"
            ),
        ),
    ]
