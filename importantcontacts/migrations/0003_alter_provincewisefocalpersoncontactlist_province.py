# Generated by Django 5.0.4 on 2024-04-26 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importantcontacts', '0002_district_mohasubordinatelist_province_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provincewisefocalpersoncontactlist',
            name='province',
            field=models.IntegerField(choices=[(1, 'Province 1'), (2, 'Province 2'), (3, 'Province 3'), (4, 'Province 4'), (5, 'Province 5'), (6, 'Province 6'), (7, 'Province 7')]),
        ),
    ]
