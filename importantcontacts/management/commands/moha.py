from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from importantcontacts.models import MohaPhoneDirectoryList, MohaSubordinateList


class Command(BaseCommand):
    help = 'Populate MohaPhoneDirectoryList and MohaSubordinateList models with dummy data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        with transaction.atomic():
            for _ in range(20):
                division_section = fake.text()
                division_section_ne = fake.text()
                phone = fake.phone_number()
                mobile = fake.phone_number()
                email = fake.email()

                MohaPhoneDirectoryList.objects.create(
                    division_section=division_section,
                    division_section_ne=division_section_ne,
                    phone=phone,
                    mobile=mobile,
                    email=email
                )

            for _ in range(20):
                name = fake.name()
                name_ne = fake.name()
                address = fake.address()
                address_ne = fake.address()
                phone = fake.phone_number()

                MohaSubordinateList.objects.create(
                    name=name,
                    name_ne=name_ne,
                    address=address,
                    address_ne=address_ne,
                    phone=phone
                )

        self.stdout.write(self.style.SUCCESS(
            'MohaPhoneDirectoryList and MohaSubordinateList models populated successfully.'))
