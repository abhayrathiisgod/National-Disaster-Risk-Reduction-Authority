# Generated by Django 5.0.4 on 2024-05-13 04:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hazard", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hazards",
            name="icon",
            field=models.ImageField(upload_to="uplods/hazard_icons/"),
        ),
    ]
