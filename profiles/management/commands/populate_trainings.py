from django.core.management.base import BaseCommand
from faker import Faker
from datetime import datetime, timedelta
from profiles.models import Trainings, TrainingOrg, TrainingCertificate


class Command(BaseCommand):
    help = 'Populate Trainings model with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        #  all training organizations and training certificates
        training_orgs = TrainingOrg.objects.all()
        training_certificates = TrainingCertificate.objects.all()

        num_records = 100  # Change this to the desired number of records

        for _ in range(num_records):
            # Generate fake data
            training_org = fake.random_element(training_orgs)
            title = fake.text(max_nb_chars=255)
            title_ne = fake.text(max_nb_chars=255)
            description = fake.paragraph()
            description_ne = fake.paragraph()
            start_date = fake.date_between(start_date='-1y', end_date='+1y')
            end_date = start_date + \
                timedelta(days=fake.random_int(min=1, max=30))

            # Create and save the Trainings instance
            training = Trainings.objects.create(
                training_org=training_org,
                title=title,
                title_ne=title_ne,
                description=description,
                description_ne=description_ne,
                start_date=start_date,
                end_date=end_date
            )

            # random training certificates
            training.training_certificate.set(fake.random_elements(
                training_certificates, length=fake.random_int(min=1, max=3)))

        self.stdout.write(self.style.SUCCESS(
            f'Successfully populated {num_records} Trainings records'))
