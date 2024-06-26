# Generated by Django 5.0.4 on 2024-04-29 10:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PublicationAuthor",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "publication_author",
                    models.CharField(
                        default="National Disaster Risk Reduction and Management Authority",
                        max_length=255,
                    ),
                ),
                (
                    "publication_author_ne",
                    models.CharField(
                        default="राष्ट्रिय विपद् जोखिम न्यूनीकरण तथा व्यवस्थापन प्राधिकरण",
                        max_length=255,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PublicationType",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "publication_type",
                    models.CharField(
                        choices=[
                            (
                                "Decision/Circular/Directive",
                                "Decision_Circular_Directive",
                            ),
                            ("Rules and Regulations", "Rules_and_Regulations"),
                            ("Policies and Directories", "Policies_and_Directories"),
                            ("Report", "Report"),
                            ("Procedure", "Procedure"),
                            ("Plan", "Plan"),
                            ("Articles", "Articles"),
                            ("Criteria", "Criteria"),
                            ("MeetingReport", "MeetingReport"),
                            ("Tender", "Tender"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "publication_type_ne",
                    models.CharField(
                        choices=[
                            ("निर्णय/सर्कुलर/निर्देशिका", "निर्णय_सर्कुलर_निर्देशिका"),
                            ("नियम तथा विनियम", "नियम_तथा_विनियम"),
                            ("नीति तथा दिशानिर्देशन", "नीति_तथा_दिशानिर्देशन"),
                            ("प्रतिवेदन", "प्रतिवेदन"),
                            ("प्रक्रिया", "प्रक्रिया"),
                            ("योजना", "योजना"),
                            ("लेख", "लेख"),
                            ("मापदण्ड", "मापदण्ड"),
                            ("बैठकको_प्रतिवेदन", "बैठकको_प्रतिवेदन"),
                            ("टेन्डर", "टेन्डर"),
                        ],
                        max_length=255,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Publications",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("title_ne", models.CharField(max_length=255)),
                ("summary", models.TextField()),
                ("summary_ne", models.TextField()),
                ("date", models.DateField()),
                ("image", models.ImageField(upload_to="uploads/publication/image")),
                ("is_published", models.BooleanField(default=False)),
                (
                    "pub_author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="publication.publicationauthor",
                    ),
                ),
                (
                    "pub_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="publication.publicationtype",
                    ),
                ),
            ],
        ),
    ]
