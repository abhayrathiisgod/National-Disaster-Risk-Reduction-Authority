# Generated by Django 5.0.4 on 2024-05-15 04:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("incident", "0041_alter_incident_createdon_alter_incident_modifiedon"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="loss",
            options={"verbose_name": "Loss", "verbose_name_plural": "Losses"},
        ),
    ]
