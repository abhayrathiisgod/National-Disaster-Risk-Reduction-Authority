# Generated by Django 5.0.4 on 2024-05-17 04:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pressnotenews", "0009_newsinfo_slug_pressnote_slug_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newsinfo",
            name="title",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="newsinfo",
            name="title_ne",
            field=models.CharField(max_length=255),
        ),
    ]