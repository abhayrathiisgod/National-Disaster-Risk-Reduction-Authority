# Generated by Django 5.0.4 on 2024-04-30 06:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("federal", "0002_district_code_district_district_name_ne_and_more"),
        ("trainingprojects", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Training",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("title_ne", models.CharField(max_length=255)),
                ("startDate", models.DateField(blank=True, null=True)),
                ("endDate", models.DateField(blank=True, null=True)),
                ("num_of_participants", models.IntegerField()),
                ("description", models.TextField()),
                ("attendants", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trainingprojects.address",
                    ),
                ),
                (
                    "district",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="federal.district",
                    ),
                ),
                (
                    "municipality",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="federal.municipality",
                    ),
                ),
                (
                    "province",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="federal.province",
                    ),
                ),
            ],
        ),
    ]
