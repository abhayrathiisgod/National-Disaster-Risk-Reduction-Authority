import random
from faker import Faker
from django.core.management.base import BaseCommand
from trainingprojects.models import Training, Address
from federal.models import Province, District, Municipality
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Populate Training model with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        addresses = Address.objects.all()
        provinces = Province.objects.all()
        districts = District.objects.all()
        municipalities = Municipality.objects.all()
        users = User.objects.all()

        for _ in range(20):

            address = random.choice(addresses)
            province = random.choice(provinces)
            district = random.choice(districts)
            municipality = random.choice(municipalities)
            user = random.choice(users)

            # Generate fake data
            title = fake.text(max_nb_chars=50)
            title_ne = fake.text(max_nb_chars=50)
            start_date = fake.date_time_between(
                start_date='-30d', end_date='+30d')
            end_date = start_date + timedelta(days=random.randint(30, 365))
            num_of_participants = random.randint(10, 50)
            description = fake.text(max_nb_chars=200)
            attendants = fake.name()

            training = Training.objects.create(
                address=address,
                title=title,
                title_ne=title_ne,
                startDate=start_date,
                endDate=end_date,
                num_of_participants=num_of_participants,
                description=description,
                attendants=attendants,
                province=province,
                district=district,
                municipality=municipality,
            )

            print(f'Created Training: {training.title}')

        print('Database populated successfully!')
