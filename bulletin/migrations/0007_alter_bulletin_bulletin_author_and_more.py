# Generated by Django 5.0.4 on 2024-05-13 05:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bulletin", "0006_alter_bulletin_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bulletin",
            name="bulletin_author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="bulletin.bulletinauthor",
            ),
        ),
        migrations.AlterField(
            model_name="bulletin",
            name="bulletin_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="bulletin.bulletintype"
            ),
        ),
    ]
