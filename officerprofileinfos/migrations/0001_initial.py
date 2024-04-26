# Generated by Django 5.0.4 on 2024-04-26 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=100)),
                ('designation_ne', models.CharField(max_length=100)),
                ('office', models.CharField(max_length=100)),
                ('office_ne', models.CharField(max_length=100)),
                ('is_executive_committee', models.BooleanField(default=False)),
                ('is_national_council', models.BooleanField(default=False)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('name_ne', models.CharField(max_length=255)),
                ('additional_info', models.TextField()),
                ('additional_info_ne', models.TextField()),
                ('image', models.URLField()),
                ('order', models.IntegerField()),
                ('designations', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officerprofileinfos.designation')),
            ],
        ),
    ]
