# Generated by Django 5.0.4 on 2024-05-13 06:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("incident", "0020_alter_incident_createdon_alter_incident_hazard_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="incident",
            name="createdOn",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 5, 13, 6, 10, 9, 21324, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="incident",
            name="modifiedOn",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 5, 13, 6, 10, 9, 21540, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
