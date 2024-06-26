# Generated by Django 5.0.4 on 2024-05-02 08:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Alerts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alertlist",
            name="event",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Earthquake", "Earthquake"),
                    ("Hurricane", "Hurricane"),
                    ("Tornado", "Tornado"),
                    ("Flood", "Flood"),
                    ("Wildfire", "Wildfire"),
                    ("Tsunami", "Tsunami"),
                    ("Volcanic eruption", "Volcanic eruption"),
                    ("Landslide", "Landslide"),
                    ("Drought", "Drought"),
                    ("Blizzard", "Blizzard"),
                    ("Heatwave", "Heatwave"),
                    ("Avalanche", "Avalanche"),
                    ("Cyclone", "Cyclone"),
                    ("Thunderstorm", "Thunderstorm"),
                    ("Hailstorm", "Hailstorm"),
                ],
                null=True,
            ),
        ),
    ]
