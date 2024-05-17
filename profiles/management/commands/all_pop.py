# core/management/commands/populate.py

from django.core.management.base import BaseCommand
from faker import Faker
import random
from profiles.models import (
    Skills, Designation, Department, TrainingOrg, TrainingCertificate, Trainings,
    OfficerProfile, CommiteProfile, NationalCouncilHead, ExecutiveCommitteHead,
    OfficersHead, OfficersSpokesPerson, InformationOfficer
)

from django_ckeditor_5.fields import CKEditor5Field

fake = Faker()


class Command(BaseCommand):
    help = 'Populate the database with fake data'

    def handle(self, *args, **kwargs):
        self.create_skills()
        self.create_designations()
        self.create_departments()
        self.create_training_orgs()
        self.create_training_certificates()
        self.create_trainings()
        self.create_officer_profiles()
        self.create_committee_profiles()
        self.create_national_council_heads()
        self.create_executive_committee_heads()
        self.create_officers_heads()
        self.create_officers_spokes_persons()
        self.create_information_officers()

    def create_skills(self):
        for _ in range(10):
            Skills.objects.create(
                title=fake.job(),
                title_ne=fake.job(),
                color=fake.color_name()
            )

    def create_designations(self):
        for _ in range(10):
            Designation.objects.create(
                designation=fake.job(),
                designation_ne=fake.job(),
                office=fake.company(),
                office_ne=fake.company(),
                is_executive_committee=fake.boolean(),
                is_national_council=fake.boolean(),
                link=fake.url()
            )

    def create_departments(self):
        for _ in range(10):
            Department.objects.create(
                title=fake.bs(),
                title_ne=fake.bs()
            )

    def create_training_orgs(self):
        for _ in range(10):
            TrainingOrg.objects.create(
                title=fake.company(),
                title_ne=fake.company()
            )

    def create_training_certificates(self):
        for _ in range(10):
            TrainingCertificate.objects.create(
                certificate=fake.url()
            )

    def create_trainings(self):
        training_orgs = list(TrainingOrg.objects.all())
        training_certificates = list(TrainingCertificate.objects.all())

        for _ in range(10):
            training = Trainings.objects.create(
                training_org=random.choice(training_orgs),
                title=fake.catch_phrase(),
                title_ne=fake.catch_phrase(),
                description=fake.text(),
                description_ne=fake.text(),
                start_date=fake.date_this_decade(),
                end_date=fake.date_this_decade()
            )
            training.training_certificate.set(
                random.sample(training_certificates, k=3))

    def create_officer_profiles(self):
        designations = list(Designation.objects.all())
        departments = list(Department.objects.all())
        skills = list(Skills.objects.all())
        trainings = list(Trainings.objects.all())

        for _ in range(10):
            profile = OfficerProfile.objects.create(
                designation=random.choice(designations),
                name=fake.name(),
                name_ne=fake.name(),
                mobile=fake.phone_number(),
                email=fake.email(),
                additional_info=fake.text()[:14],
                additional_info_ne=fake.text(),
                image=fake.image_url(),
                from_date=fake.date_this_decade(),
                to_date=fake.date_this_decade(),
                order=random.randint(1, 10)
            )
            profile.departments.set(random.sample(departments, k=2))
            profile.skills.set(random.sample(skills, k=3))
            profile.trainings.set(random.sample(trainings, k=2))

    def create_committee_profiles(self):
        designations = list(Designation.objects.all())

        for _ in range(10):
            CommiteProfile.objects.create(
                designation=random.choice(designations),
                name=fake.name(),
                name_ne=fake.name(),
                additional_info=fake.text(),
                additional_info_ne=fake.text(),
                image=fake.image_url(),
                order=random.randint(1, 10)
            )

    def create_national_council_heads(self):
        designations = list(Designation.objects.all())

        for _ in range(10):
            NationalCouncilHead.objects.create(
                designation=random.choice(designations),
                name=fake.name(),
                name_ne=fake.name(),
                additional_info=fake.text(),
                additional_info_ne=fake.text(),
                image=fake.image_url(),
                order=random.randint(1, 10)
            )

    def create_executive_committee_heads(self):
        designations = list(Designation.objects.all())

        for _ in range(10):
            ExecutiveCommitteHead.objects.create(
                designation=random.choice(designations),
                name=fake.name(),
                name_ne=fake.name(),
                additional_info=fake.text(),
                additional_info_ne=fake.text(),
                image=fake.image_url(),
                order=random.randint(1, 10)
            )

    def create_officers_heads(self):
        designations = list(Designation.objects.all())

        for _ in range(10):
            OfficersHead.objects.create(
                designation=random.choice(designations),
                name=fake.name(),
                name_ne=fake.name(),
                additional_info=fake.text(),
                additional_info_ne=fake.text(),
                image=fake.image_url(),
                order=random.randint(1, 10)
            )

    def create_officers_spokes_persons(self):
        designations = list(Designation.objects.all())

        for _ in range(10):
            OfficersSpokesPerson.objects.create(
                designation=random.choice(designations),
                name=fake.name(),
                name_ne=fake.name(),
                additional_info=fake.text(),
                additional_info_ne=fake.text(),
                image=fake.image_url(),
                order=random.randint(1, 10)
            )

    def create_information_officers(self):
        designations = list(Designation.objects.all())

        for _ in range(10):
            InformationOfficer.objects.create(
                designation=random.choice(designations),
                name=fake.name(),
                name_ne=fake.name(),
                additional_info=fake.text(),
                additional_info_ne=fake.text(),
                image=fake.image_url(),
                order=random.randint(1, 10)
            )
