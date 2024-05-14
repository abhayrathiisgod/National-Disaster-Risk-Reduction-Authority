from django.core.management.base import BaseCommand
from faker import Faker
from importantcontacts.models import SnakeBites
from federal.models import District


class Command(BaseCommand):
    help = 'Populate SnakeBites model with dummy data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        districts = District.objects.all()

        for _ in range(32):  # Adjust the range as needed
            district = fake.random_element(districts)
            treatment_centre = fake.company()
            treatment_centre_ne = fake.company()

            SnakeBites.objects.create(
                treatment_centre=treatment_centre,
                treatment_centre_ne=treatment_centre_ne,
                district=district
            )

        self.stdout.write(self.style.SUCCESS(
            'SnakeBites model populated successfully.'))
