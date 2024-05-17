# management/commands/populate_data.py
import os
import random
from django.core.management.base import BaseCommand
from faker import Faker
from trainingprojects.models import fiscal, GeoHazardAssessment
from federal.models import Province, District, Municipality

fake = Faker()


class Command(BaseCommand):
    help = 'Populate data using Faker'

    def handle(self, *args, **kwargs):
        self.populate_fiscal()
        self.populate_geo_hazard_assessment()

    def populate_fiscal(self):
        fiscal.objects.all().delete()  # Clear existing data
        for _ in range(5):
            year = fake.year()
            year_ne = fake.year()
            fiscal.objects.create(year=year, year_ne=year_ne)

    def populate_geo_hazard_assessment(self):
        GeoHazardAssessment.objects.all().delete()  # Clear existing data
        fiscal_years = fiscal.objects.all()
        provinces = Province.objects.all()
        districts = District.objects.all()
        municipalities = Municipality.objects.all()
        for _ in range(20):
            fiscal_year = random.choice(fiscal_years)
            title = fake.sentence()
            title_ne = fake.sentence()
            province = random.choice(provinces)
            district = random.choice(districts)
            municipality = random.choice(municipalities)
            GeoHazardAssessment.objects.create(
                fiscal_year=fiscal_year,
                title=title,
                title_ne=title_ne,
                province=province,
                district=district,
                municipality=municipality
            )
