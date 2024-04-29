# Generated by Django 5.0.4 on 2024-04-29 04:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NewsInfo",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.TextField()),
                ("title_ne", models.TextField()),
                ("description", models.TextField()),
                ("description_ne", models.TextField()),
                ("summary", models.TextField()),
                ("summary_ne", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("image", models.ImageField(upload_to="uploads/news_info")),
            ],
        ),
    ]
