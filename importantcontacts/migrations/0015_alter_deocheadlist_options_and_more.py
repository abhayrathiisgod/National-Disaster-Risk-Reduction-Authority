# Generated by Django 5.0.4 on 2024-05-15 04:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "importantcontacts",
            "0014_alter_deocheadlist_id_alter_emergencyvehicle_id_and_more",

        ),

    ]

    operations = [
        migrations.AlterModelOptions(
            name="deocheadlist",
            options={
                "verbose_name": "Deoc Head",
                "verbose_name_plural": "Deoc Head List",
            },
        ),
        migrations.AlterModelOptions(
            name="localdisastermanagementcontactlist",
            options={
                "verbose_name": "Local Disaster Management Contact",
                "verbose_name_plural": "Local Disaster Management Contact List",
            },
        ),
        migrations.AlterModelOptions(
            name="mohaphonedirectorylist",
            options={
                "verbose_name": "Moha Phone Directory",
                "verbose_name_plural": "Moha Phone Directory List",
            },
        ),
        migrations.AlterModelOptions(
            name="mohasubordinatelist",
            options={
                "verbose_name": "Moha Subordinate",
                "verbose_name_plural": "Moha Subordinate List",
            },
        ),
        migrations.AlterModelOptions(
            name="provincewisefocalpersoncontactlist",
            options={
                "verbose_name": "Province Wise Focal Person Contact",
                "verbose_name_plural": "Province Wise Focal Person Contact List",
            },
        ),
        migrations.AlterModelOptions(
            name="snakebites",
            options={
                "verbose_name": "Snake Bite",
                "verbose_name_plural": "Snake Bite List",
            },
        ),
    ]
