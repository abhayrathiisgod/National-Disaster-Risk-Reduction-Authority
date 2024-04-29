# Generated by Django 5.0.4 on 2024-04-29 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pressnotenews", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("Author_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField()),
                ("name_ne", models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name="Type",
            fields=[
                ("Type_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField()),
                ("name_ne", models.CharField()),
            ],
        ),
        migrations.AddField(
            model_name="newsinfo",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="pressnotenews.author",
            ),
        ),
        migrations.AddField(
            model_name="newsinfo",
            name="type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="pressnotenews.type",
            ),
        ),
    ]
