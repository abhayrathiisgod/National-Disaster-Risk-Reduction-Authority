from django.core.management.base import BaseCommand
from bulletin.models import Bulletin, BulletinAuthor, BulletinType
from faker import Faker
import random


class Command(BaseCommand):
    help = 'populating bulletins model'

    def handle(self, *args, **kwargs):
        fake = Faker()
        author = BulletinAuthor.objects.first()
        # type1 = BulletinType.objects.first()
        # type2 = BulletinType.objects.last()
        typee = BulletinType.objects.all()
        for _ in range(20):
            bulletin = Bulletin.objects.create(
                bulletin_author=author,
                bulletin_type=random.choice(typee),
                title=fake.text()[:50],
                title_ne=fake.text()[:50],
                summary=fake.text()[:50],
                summary_ne=fake.text()[:50],
                description=fake.text()[:50],
                description_ne=fake.text()[:50],
                file='uploads/bulletin/files/mit18_s096iap23_lec7.pdf',
                image='uploads/bulletin/Daily Bulletin (08-12-2023)/prof.jpeg'

            )

            bulletin.save()

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated bulletins'))
