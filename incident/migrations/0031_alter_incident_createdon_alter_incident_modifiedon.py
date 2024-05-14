# Generated by Django 5.0.4 on 2024-05-14 04:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("incident", "0030_alter_incident_createdon_alter_incident_modifiedon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="incident",
            name="createdOn",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 5, 14, 4, 13, 32, 960628, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="incident",
            name="modifiedOn",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 5, 14, 4, 13, 32, 960774, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
