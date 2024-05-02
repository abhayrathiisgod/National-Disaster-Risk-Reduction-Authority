from typing import Any
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
from random import choice

from profiles.models import Skills, Designation, Department, TrainingOrg, TrainingCertificate, Trainings, OfficerProfile, CommiteProfile


class Command(BaseCommand):
    help = 'Populate Skills model with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        num_records = 10

        skills_en = [
            "Programming",
            "Problem Solving",
            "Communication",
            "Time Management",
            "Leadership",
            "Teamwork",
            "Creativity",
            "Adaptability",
            "Critical Thinking",
            "Attention to Detail"
        ]

        # Nepali skills
        skills_ne = [
            "प्रोग्रामिङ",
            "समस्या समाधान",
            "संचार",
            "समय प्रबंधन",
            "नेतृत्व",
            "साझेदारी",
            "सृजनात्मकता",
            "अनुकूलनशीलता",
            "महत्वपूर्ण विचार",
            "विवेकशीलता"
        ]

        for i in range(num_records):
            color = fake.color_name()
            Skills.objects.create(
                title=skills_en[i], title_ne=skills_ne[i], color=color)

        self.stdout.write(self.style.SUCCESS(
            f'Successfully populated {num_records} Skills records'))

        num_records = 10
        # designation
        for _ in range(num_records):
            designation = fake.job()
            designation_ne = fake.job()
            office = fake.company()
            office_ne = fake.company()
            is_executive_committee = fake.boolean()
            is_national_council = fake.boolean()
            link = fake.url()

            Designation.objects.create(designation=designation, designation_ne=designation_ne,
                                       office=office, office_ne=office_ne,
                                       is_executive_committee=is_executive_committee,
                                       is_national_council=is_national_council,
                                       link=link)

        num_records = 15
        departments = [
            "Ministry of Health and Population",
            "Ministry of Education",
            "Ministry of Finance",
            "Ministry of Agriculture",
            "Ministry of Social Welfare",
            "Ministry of Science and Technology",
            "Ministry of Foreign Affairs",
            "Ministry of Forests and Environment",
            "Ministry of Economy",
            "Ministry of Justice",
            "Ministry of Organization",
            "Ministry of Tourism and Aviation",
            "Ministry of Communication and Information Technology",
            "Ministry of Roads and Transport",
            "Ministry of Culture, Tourism, and Civil Aviation"
        ]
        departments_ne = [
            "स्वास्थ्य तथा जनसंख्या मन्त्रालय",
            "शिक्षा मन्त्रालय",
            "वित्त मन्त्रालय",
            "कृषि मन्त्रालय",
            "सामाजिक कार्य मन्त्रालय",
            "विज्ञान तथा प्रविधि मन्त्रालय",
            "विदेश मन्त्रालय",
            "वन तथा पारिस्थितिकी मन्त्रालय",
            "आर्थिक मन्त्रालय",
            "न्याय मन्त्रालय",
            "संगठन मन्त्रालय",
            "पर्यटन तथा उड्डयन मन्त्रालय",
            "संचार तथा सूचना प्रविधि मन्त्रालय",
            "सडक तथा यातायात मन्त्रालय",
            "कला, सांस्कृतिक तथा परिकर कला मन्त्रालय"
        ]
        # Populate Department model
        num_records = min(len(departments), len(departments_ne))

        # Populate Department model
        for i in range(num_records):
            Department.objects.create(
                title=departments[i], title_ne=departments_ne[i])

        # Populate TrainingOrg model
        for _ in range(num_records):
            title = fake.text(max_nb_chars=255)
            title_ne = fake.text(max_nb_chars=255)

            TrainingOrg.objects.create(title=title, title_ne=title_ne)

        # Populate TrainingCertificate model
        for _ in range(num_records):
            certificate = fake.url()

            TrainingCertificate.objects.create(certificate=certificate)

        self.stdout.write(self.style.SUCCESS(f'Successfully populated {
                          num_records} records each for Designation, Department, TrainingOrg, and TrainingCertificate'))
