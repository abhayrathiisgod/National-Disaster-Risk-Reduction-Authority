from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from importantcontacts.models import LocalDisasterManagementContactList
from federal.models import Province, District, Municipality


class Command(BaseCommand):
    help = 'Populate LocalDisasterManagementContactList model with dummy data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        with transaction.atomic():
            provinces = Province.objects.all()
            districts = District.objects.all()
            municipalities = Municipality.objects.all()

            for _ in range(10):  # Adjust the range as needed
                province = fake.random_element(provinces)
                district = fake.random_element(districts)
                municipality = fake.random_element(municipalities)

                email = fake.email()
                contact_num = fake.phone_number()

                LocalDisasterManagementContactList.objects.create(
                    email=email,
                    contact_num=contact_num,
                    province=province,
                    district=district,
                    municcipality=municipality
                )

        self.stdout.write(self.style.SUCCESS(
            'LocalDisasterManagementContactList model populated successfully.'))
