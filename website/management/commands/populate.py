import random
from faker import Faker
from django.core.management.base import BaseCommand
from website.models import NdrmaPortals, Menu, Bookmarks, Page, FrequentlyAskedQuestions, WardDocument


class Command(BaseCommand):
    help = 'Populate models with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Populate NdrmaPortals
        for _ in range(10):
            name = fake.company()
            image = 'ndrmaPortal/icons/blank_profile.png'
            realted_link = fake.url()
            NdrmaPortals.objects.create(
                name=name, image=image, realted_link=realted_link)

        # Populate Menu
        for _ in range(10):
            name = fake.word()
            name_ne = fake.word()
            parent = None
            link = fake.url() if random.choice([True, False]) else None
            is_external_link = random.choice([True, False])
            content_source = None
            page = fake.word() if random.choice([True, False]) else None
            Menu.objects.create(name=name, name_ne=name_ne, parent=parent, link=link,
                                is_external_link=is_external_link, content_source=content_source, page=page)

        # Populate Bookmarks
        for _ in range(10):
            name = fake.word()
            name_ne = fake.word()
            link = fake.url()
            Bookmarks.objects.create(name=name, name_ne=name_ne, link=link)

        # Populate Page
        for _ in range(10):
            title = fake.sentence()
            title_ne = fake.sentence()

            description = fake.text()
            description_ne = fake.text()
            slug = fake.slug()
            Page.objects.create(title=title, title_ne=title_ne,
                                description=description, description_ne=description_ne, slug=slug)

        # Populate FrequentlyAskedQuestions
        for _ in range(10):
            question = fake.sentence()
            question_ne = fake.sentence()
            answer = fake.paragraph()
            answer_ne = fake.paragraph()
            FrequentlyAskedQuestions.objects.create(question=question, question_ne=question_ne,
                                                    answer=answer, answer_ne=answer_ne)

        # Populate WardDocument
        for _ in range(10):
            filename = fake.file_name()
            filename_ne = fake.file_name()
            document = 'uploads/ward_document/100-toefl-reading-practice-questions.pdf'

            WardDocument.objects.create(filename=filename, filename_ne=filename_ne,
                                        document=document)

        self.stdout.write(self.style.SUCCESS('Models populated successfully!'))
