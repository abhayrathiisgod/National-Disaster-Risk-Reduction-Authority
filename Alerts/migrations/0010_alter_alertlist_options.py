# Generated by Django 5.0.4 on 2024-05-16 11:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Alerts", "0009_alter_alertlist_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="alertlist",
            options={"verbose_name": "Alert", "verbose_name_plural": "Alert List"},
        ),
    ]