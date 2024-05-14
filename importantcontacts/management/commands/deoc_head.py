from django.db import transaction
from django.core.management.base import BaseCommand
from faker import Faker
from importantcontacts.models import DeocHeadList, District


class Command(BaseCommand):
    help = 'Populate DeocHeadList model with dummy data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        with transaction.atomic():
            districts = District.objects.all()  # Retrieve all District objects

            for _ in range(10):  # Adjust the range as needed
                # Select a random District object
                district = fake.random_element(districts)

                designation = fake.job()
                designation_ne = fake.job()
                office_landline_no = fake.phone_number()
                fax_no = fake.phone_number()
                mobile_no = fake.phone_number()

                DeocHeadList.objects.create(
                    district=district,
                    designation=designation,
                    designation_ne=designation_ne,
                    office_landline_no=office_landline_no,
                    fax_no=fax_no,
                    mobile_no=mobile_no
                )

        self.stdout.write(self.style.SUCCESS(
            'DeocHeadList model populated successfully.'))
