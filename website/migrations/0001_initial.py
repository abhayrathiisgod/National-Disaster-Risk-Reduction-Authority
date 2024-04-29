# Generated by Django 5.0.4 on 2024-04-29 04:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactDetail",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("detail", models.TextField()),
                ("detail_ne", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="FrequentlyAskedQuestions",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("question", models.TextField()),
                ("question_ne", models.TextField()),
                ("answer", models.TextField()),
                ("answer_ne", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Introduction",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.TextField()),
                ("title_ne", models.TextField()),
                ("description", models.TextField()),
                ("description_ne", models.TextField()),
                ("sub_title", models.TextField()),
                ("sub_title_ne", models.TextField()),
                ("content", models.TextField()),
                ("content_ne", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="WardDocument",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("filename", models.CharField(max_length=255)),
                ("filename_ne", models.CharField(max_length=255)),
                ("document", models.FileField(upload_to="uploads/ward_document")),
                ("file_extension", models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]