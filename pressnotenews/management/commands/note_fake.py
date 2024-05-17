from django.core.management.base import BaseCommand
from faker import Faker
from pressnotenews.models import Author, Type, NewsInfo, PressNote


class Command(BaseCommand):
    help = 'Populate the database with initial data using Faker'

    def handle(self, *args, **kwargs):
        self.populate_authors()
        self.populate_types()
        self.populate_news_info()
        self.populate_press_notes()

    def populate_authors(self):
        faker = Faker()
        for _ in range(5):
            Author.objects.create(
                name=faker.name(),
                name_ne=faker.name(),
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated Authors'))

    def populate_types(self):
        faker = Faker()
        for _ in range(3):
            Type.objects.create(
                name=faker.word(),
                name_ne=faker.word(),
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated Types'))

    def populate_news_info(self):
        faker = Faker()
        authors = list(Author.objects.all())
        for _ in range(5):
            NewsInfo.objects.create(
                title=faker.sentence(),
                title_ne=faker.sentence(),
                description=faker.paragraph(),
                description_ne=faker.paragraph(),
                summary=faker.paragraph(),
                summary_ne=faker.paragraph(),
                image=faker.image_url(),
            )
        self.stdout.write(self.style.SUCCESS(
            'Successfully populated NewsInfo'))

    def populate_press_notes(self):
        faker = Faker()
        authors = list(Author.objects.all())
        types = list(Type.objects.all())
        for _ in range(5):
            PressNote.objects.create(
                author=faker.random_element(authors),
                type=faker.random_element(types),
                title=faker.sentence(),
                title_ne=faker.sentence(),
                description=faker.paragraph(),
                description_ne=faker.paragraph(),
                summary=faker.paragraph(),
                summary_ne=faker.paragraph(),
                image=faker.image_url(),
                file=faker.file_path(extension='pdf'),
            )
        self.stdout.write(self.style.SUCCESS(
            'Successfully populated PressNote'))
