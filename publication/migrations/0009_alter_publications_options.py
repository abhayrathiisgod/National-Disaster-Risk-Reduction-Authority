# Generated by Django 5.0.4 on 2024-05-15 04:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "publication",
            "0008_alter_publicationauthor_id_alter_publications_id_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="publications",
            options={
                "verbose_name": "Publication",
                "verbose_name_plural": "Publications",
            },
        ),
    ]
