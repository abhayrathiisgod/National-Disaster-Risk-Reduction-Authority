from django.core.management.base import BaseCommand
from guidecourse.models import GuideCourse, Guidechildren, Course
from faker import Faker


class Command(BaseCommand):
    help = 'Populate the database with initial data using Faker'

    def handle(self, *args, **kwargs):
        self.populate_guide_courses()
        self.populate_guide_children()
        self.populate_courses()

    def populate_guide_courses(self):
        faker = Faker()
        for _ in range(5):
            GuideCourse.objects.create(
                name=faker.word(),
                title=faker.sentence(),
                title_ne=faker.sentence(),
                description=faker.text(),
                description_ne=faker.text(),
                image=faker.image_url(),
            )
        self.stdout.write(self.style.SUCCESS(
            'Successfully populated GuideCourse'))

    def populate_guide_children(self):
        faker = Faker()
        guide_courses = list(GuideCourse.objects.all())

        for _ in range(10):
            guide_child = Guidechildren.objects.create(
                name=faker.word(),
                name_ne=faker.word(),
                title=faker.sentence(),
                title_ne=faker.sentence(),
                description=faker.text(),
                description_ne=faker.text(),
                image=faker.image_url(),
            )
            guide_child.parent.set(faker.random_elements(
                elements=guide_courses, length=2))

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated Guidechildren'))

    def populate_courses(self):
        faker = Faker()
        for _ in range(5):
            Course.objects.create(
                title=faker.sentence(),
                title_ne=faker.sentence(),
                path=faker.url(),
                image=faker.image_url(),
                youtube_url=faker.url(),
                description=faker.text(),
                description_ne=faker.text(),
                target_audience=faker.text(),
                target_audience_ne=faker.text(),
                duration=faker.time(),
                skill_level=faker.random_element(
                    elements=['beginner', 'intermediate', 'advanced']),
                language=faker.random_element(elements=['English', 'Nepali']),
                learning_objective=faker.text(),
                learning_objective_ne=faker.text(),
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Courses'))
