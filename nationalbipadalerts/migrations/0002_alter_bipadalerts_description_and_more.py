# Generated by Django 5.0.4 on 2024-05-14 03:44

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("nationalbipadalerts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bipadalerts",
            name="description",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Text"
            ),
        ),
        migrations.AlterField(
            model_name="bipadalerts",
            name="description_ne",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Text"
            ),
        ),
    ]
