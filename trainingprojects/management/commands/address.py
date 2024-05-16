import random
from faker import Faker
from django.core.management.base import BaseCommand
from trainingprojects.models import Address


class Command(BaseCommand):
    help = 'Populate Address model with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(20):
            local_address = fake.address()
            local_address_ne = fake.address()

            address = Address.objects.create(
                local_address=local_address,
                local_address_ne=local_address_ne
            )

            print(f'Created Address: {address.local_address}')

        print('Database populated successfully!')
