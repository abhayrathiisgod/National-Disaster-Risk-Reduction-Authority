# Generated by Django 5.0.4 on 2024-05-17 07:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0018_alter_page_title_alter_page_title_ne"),
    ]

    operations = [
        migrations.AlterField(
            model_name="introduction",
            name="title",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="introduction",
            name="title_ne",
            field=models.CharField(max_length=255),
        ),
    ]
