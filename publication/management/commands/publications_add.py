import os
import django
import random
from faker import Faker
from django.core.management.base import BaseCommand
from publication.models import Publications, PublicationType, PublicationAuthor


class Command(BaseCommand):
    help = 'Populate Publications module with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Populate Publications
        for _ in range(20, 40):
            pub_type = random.choice(PublicationType.objects.all())
            pub_author = random.choice(PublicationAuthor.objects.all())
            title = fake.sentence()[:50]
            title_ne = fake.sentence()[:50]
            description = fake.paragraph()
            description_ne = fake.paragraph()
            summary = fake.paragraph()
            summary_ne = fake.paragraph()
            date = fake.date()
            pdffile = 'uploads/publication/pdf/Three_specific_good_civil_data..pdf'

            is_published = fake.boolean()

            publication = Publications.objects.create(
                pub_type=pub_type,
                pub_author=pub_author,
                title=title,
                title_ne=title_ne,
                description=description,
                description_ne=description_ne,
                summary=summary,
                summary_ne=summary_ne,
                date=date,
                pdffile=pdffile,
                is_published=is_published
            )

            print(f'Created Publication: {publication.title}')

        print('Database populated successfully!')
