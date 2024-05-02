import random
from django.utils import timezone
from django.core.management.base import BaseCommand
from faker import Faker
from federal.models import Ward
from hazard.models import Hazards
from incident.models import Loss, Incident
from django.contrib.auth.models import User

fake = Faker()


class Command(BaseCommand):
    help = 'Populate Loss and Incident models with fake data'

    def handle(self, *args, **kwargs):
        # Populate Loss model
        for _ in range(50):  # Adjust the range as needed
            Loss.objects.create(
                peopleDeathCount=random.randint(0, 50),
                peopleDeathMaleCount=random.randint(0, 30),
                peopleDeathFemaleCount=random.randint(0, 20),
                peopleDeathOtherCount=random.randint(0, 5),
                peopleDeathUnknownCount=random.randint(0, 10),
                peopleDeathDisabledCount=random.randint(0, 5),
                peopleMissingCount=random.randint(0, 20),
                peopleMissingMaleCount=random.randint(0, 15),
                peopleMissingFemaleCount=random.randint(0, 10),
                peopleMissingOtherCount=random.randint(0, 3),
                peopleMissingUnknownCount=random.randint(0, 5),
                peopleMissingDisabledCount=random.randint(0, 3),
                peopleInjuredCount=random.randint(0, 100),
                peopleInjuredMaleCount=random.randint(0, 60),
                peopleInjuredFemaleCount=random.randint(0, 40),
                peopleInjuredOtherCount=random.randint(0, 10),
                peopleInjuredUnknownCount=random.randint(0, 20),
                peopleInjuredDisabledCount=random.randint(0, 10),
                peopleAffectedCount=random.randint(0, 200),
                familyAffectedCount=random.randint(0, 100),
                familyRelocatedCount=random.randint(0, 50),
                familyEvacuatedCount=random.randint(0, 50),
                livestockDestroyedCount=random.randint(0, 500),
                infrastructureDestroyedCount=random.randint(0, 50),
                infrastructureDestroyedHouseCount=random.randint(0, 20),
                infrastructureAffectedHouseCount=random.randint(0, 30),
                infrastructureDestroyedRoadCount=random.randint(0, 10),
                infrastructureAffectedRoadCount=random.randint(0, 15),
                infrastructureDestroyedBridgeCount=random.randint(0, 5),
                infrastructureAffectedBridgeCount=random.randint(0, 8),
                infrastructureDestroyedElectricityCount=random.randint(0, 5),
                infrastructureAffectedElectricityCount=random.randint(0, 8),
                infrastructureEconomicLoss=random.uniform(10000, 1000000),
                agricultureEconomicLoss=random.uniform(10000, 1000000),
                createdOn=fake.date_time_this_decade(),
                modifiedOn=timezone.now(),
                description=fake.paragraph(),
                estimatedLoss=random.uniform(10000, 1000000)
            )

        # Populate Incident model
        wards = list(Ward.objects.all())
        hazards = list(Hazards.objects.all())
        users = list(User.objects.all())

        for _ in range(50):  # Adjust the range as needed
            incident = Incident.objects.create(
                title=fake.sentence(),
                point=fake.word(),
                # createdOn=timezone.now(),
                # modifiedOn=timezone.now(),
                titleNe=fake.sentence(),
                description=fake.paragraph(),
                cause=fake.paragraph(),
                verified=fake.boolean(),
                verificationMessage=fake.paragraph(),
                approved=fake.boolean(),
                polygon=fake.word(),
                incidentOn=timezone.now(),
                reportedOn=timezone.now(),
                streetAddress=fake.street_address(),
                detail=fake.paragraph(),
                needFollowup=fake.boolean(),
                region=fake.word(),
                regionId=random.randint(1, 10),
                dataSourceId=random.randint(100, 200),
                dataSource=fake.word(),
                source=random.choice(
                    ['Nepal_police', 'Initial Rapid Assessment', 'Other']),
                hazard=random.choice(hazards),
                loss=random.choice(Loss.objects.all()),
                createdBy=random.choice(users),
                updatedBy=random.choice(users)
            )
            # Ensure sample size is within bounds
            num_wards = min(len(wards), random.randint(1, 5))
            incident.wards.set(random.sample(wards, num_wards))
