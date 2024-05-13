# Generated by Django 5.0.4 on 2024-05-13 05:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("publication", "0005_alter_publications_pub_author_and_more"),
        ("website", "0007_alter_homepagebanner_image_alter_page_featured_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="content_source",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="publication.publications",
            ),
        ),
        migrations.AlterField(
            model_name="menu",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="children",
                to="website.menu",
            ),
        ),
    ]