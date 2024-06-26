# Generated by Django 5.0.4 on 2024-04-26 06:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importantcontacts', '0005_alter_mohaphonedirectorylist_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mohaphonedirectorylist',
            name='email',
            field=models.EmailField(
                blank=True, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mohaphonedirectorylist',
            name='mobile',
            field=models.CharField(
                blank=True, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mohaphonedirectorylist',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='mohasubordinatelist',
            name='phone',
            field=models.TextField(blank=True),
            preserve_default=False,
        ),
    ]
