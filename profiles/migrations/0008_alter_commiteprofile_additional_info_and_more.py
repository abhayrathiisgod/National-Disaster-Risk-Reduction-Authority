# Generated by Django 5.0.4 on 2024-05-14 03:44

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0007_alter_commiteprofile_designation_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commiteprofile",
            name="additional_info",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Text"
            ),
        ),
        migrations.AlterField(
            model_name="commiteprofile",
            name="additional_info_ne",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Text"
            ),
        ),
        migrations.AlterField(
            model_name="executivecommittehead",
            name="additional_info",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Text"
            ),
        ),
        migrations.AlterField(
            model_name="executivecommittehead",
            name="additional_info_ne",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Text"
            ),
        ),
        migrations.AlterField(
            model_name="informationofficer",
            name="additional_info",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Text"
            ),
        ),
        migrations.AlterField(
            model_name="informationofficer",
            name="additional_info_ne",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Text"
            ),
        ),
        migrations.AlterField(
            model_name="nationalcouncilhead",
            name="additional_info",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Text"
            ),
        ),
        migrations.AlterField(
            model_name="nationalcouncilhead",
            name="additional_info_ne",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Text"
            ),
        ),
        migrations.AlterField(
            model_name="officerprofile",
            name="additional_info",
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
        ),
        migrations.AlterField(
            model_name="officerprofile",
            name="additional_info_ne",
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
        ),
        migrations.AlterField(
            model_name="officershead",
            name="additional_info",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Text"
            ),
        ),
        migrations.AlterField(
            model_name="officershead",
            name="additional_info_ne",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Text"
            ),
        ),
        migrations.AlterField(
            model_name="officersspokesperson",
            name="additional_info",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Text"
            ),
        ),
        migrations.AlterField(
            model_name="officersspokesperson",
            name="additional_info_ne",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, null=True, verbose_name="Text"
            ),
        ),
        migrations.AlterField(
            model_name="trainings",
            name="description",
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
        ),
        migrations.AlterField(
            model_name="trainings",
            name="description_ne",
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name="Text"),
        ),
    ]
