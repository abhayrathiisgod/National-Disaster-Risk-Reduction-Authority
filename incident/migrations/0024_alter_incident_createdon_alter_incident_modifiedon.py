# Generated by Django 5.0.4 on 2024-05-14 03:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("incident", "0023_alter_incident_createdon_alter_incident_modifiedon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="incident",
            name="createdOn",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 5, 14, 3, 29, 9, 355893, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="incident",
            name="modifiedOn",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 5, 14, 3, 29, 9, 356042, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
