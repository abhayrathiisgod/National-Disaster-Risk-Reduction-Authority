# Generated by Django 5.0.4 on 2024-05-02 04:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0002_alter_department_title_alter_department_title_ne_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="designation",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
