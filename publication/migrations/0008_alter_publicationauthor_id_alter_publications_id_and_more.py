# Generated by Django 5.0.4 on 2024-05-14 03:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("publication", "0007_alter_publications_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publicationauthor",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="publications",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="publicationtype",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
