from django.core.management.base import BaseCommand
from faker import Faker
from hazard.models import Hazards


class Command(BaseCommand):
    help = 'Populate Hazards model with dummy data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for order in range(3, 20):  # Adjust the range as needed
            title = fake.word()
            title_en = fake.word()
            title_ne = fake.word()
            description = fake.paragraph()
            color = fake.color_name()
            hazard_type = fake.random_element(
                elements=['Natural', 'Non-Natural'])
            icon = 'core/hazard_icons/11172_10151304564894290_974716403_n.jpg'

            Hazards.objects.create(
                title=title,
                title_en=title_en,
                title_ne=title_ne,
                order=order,
                description=description,
                icon=icon,
                color=color,
                type=hazard_type
            )

        self.stdout.write(self.style.SUCCESS(
            'Hazards model populated successfully.'))
