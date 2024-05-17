from django.core.management.base import BaseCommand
from nationalbipadalerts.models import ImportantLinks, BipadAlerts
from profiles.models import OfficerProfile
from faker import Faker


class Command(BaseCommand):
    help = 'Populate the database with initial data using Faker'

    def handle(self, *args, **kwargs):
        self.populate_important_links()
        self.populate_bipad_alerts()

    def populate_important_links(self):
        faker = Faker()
        for _ in range(5):
            ImportantLinks.objects.create(
                name=faker.company(),
                link=faker.url(),
            )
        self.stdout.write(self.style.SUCCESS(
            'Successfully populated ImportantLinks'))

    def populate_bipad_alerts(self):
        faker = Faker()
        important_links = list(ImportantLinks.objects.all())
        officer_profiles = list(OfficerProfile.objects.all())

        for _ in range(5):
            bipad_alert = BipadAlerts.objects.create(
                title=faker.sentence(),
                title_ne=faker.sentence(),
                description=faker.text(),
                description_ne=faker.text(),
                last_updated=faker.date_time_this_year(),
            )
            bipad_alert.important_links.set(
                faker.random_elements(elements=important_links, length=2))
            bipad_alert.important_numbers.set(
                faker.random_elements(elements=officer_profiles, length=2))

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated BipadAlerts'))
