import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from trainingprojects.models import Donater


class Command(BaseCommand):
    help = 'Populate Donater model with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        user_ids = User.objects.values_list('id', flat=True)

        for _ in range(20):
            name = fake.name()
            link = fake.url()
            donater_created_by_id = random.choice(user_ids)
            donater_updated_by_id = random.choice(user_ids)

            donater = Donater.objects.create(
                name=name,
                link=link,
                donater_created_by_id=donater_created_by_id,
                donater_updated_by_id=donater_updated_by_id
            )

            print(f'Created Donater: {donater.name}')

        print('Database populated successfully!')
