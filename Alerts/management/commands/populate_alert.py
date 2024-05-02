import random
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker
from hazard.models import Hazards
from federal.models import Ward
from Alerts.models import AlertList

fake = Faker()


class Command(BaseCommand):
    help = 'Populate AlertList model with fake data'
    # total = 100

    def add_arguments(self, parser):
        parser.add_argument(
            'total', type=int, help=' number of alerts to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        ward_ids = [101, 301, 1001]

        # Filter wards based on the specified ward IDs
        wards = Ward.objects.filter(id__in=ward_ids)
        hazards = Hazards.objects.all()
        users = User.objects.all()

        for _ in range(total):
            alert = AlertList.objects.create(
                title=fake.sentence(),
                titleNe=fake.sentence(),
                source=fake.company(),
                description=fake.paragraph(),
                verified=fake.boolean(),
                public=fake.boolean(),
                startedOn=fake.date_time_this_decade(),
                expireOn=timezone.now() + timezone.timedelta(days=random.randint(1, 30)),
                polygon=fake.word(),
                referenceType=fake.word(),
                referenceData=fake.text(),
                referenceId=random.randint(1, 100),
                region=fake.word(),
                regionId=random.randint(1, 10),
                hazard=random.choice(hazards),
                event=random.choice([choice[0]
                                     for choice in AlertList.DISASTER_TYPES])
            )
        # Select random wards from the filtered wards
        random_wards = 101

        self.stdout.write(self.style.SUCCESS(
            f'{total} alerts created successfully!'))
