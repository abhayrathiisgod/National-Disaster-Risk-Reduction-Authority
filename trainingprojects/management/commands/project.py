import random
from faker import Faker
from django.core.management.base import BaseCommand
from trainingprojects.models import Project, Address, Donater
from django.contrib.auth.models import User
from federal.models import District
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Populate Project model with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        users = User.objects.all()
        addresses = Address.objects.all()
        donaters = Donater.objects.all()
        districts = District.objects.all()

        for _ in range(20):

            user = random.choice(users)
            address = random.choice(addresses)
            donater = random.choice(donaters)
            district = random.choice(districts)
            title = fake.text(max_nb_chars=50)
            title_ne = fake.text(max_nb_chars=50)
            budget = fake.random_number(5)
            budget_ne = fake.random_number(5)
            start_date = fake.date_time_between(
                start_date='-30d', end_date='+30d')
            end_date = start_date + timedelta(days=random.randint(30, 365))

            project = Project.objects.create(
                address=address,
                donor=donater,
                title=title,
                title_ne=title_ne,
                budget=budget,
                budget_ne=budget_ne,
                start_date=start_date,
                end_date=end_date,
                created_by=user,
                updated_by=user,
                district=district
            )

            print(f'Created Project: {project.title}')

        print('Database populated successfully!')
