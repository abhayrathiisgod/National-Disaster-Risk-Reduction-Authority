from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker
from importantcontacts.models import ProvinceWiseFocalPersonContactList, MohaPhoneDirectoryList, Province


class Command(BaseCommand):
    help = 'Populate ProvinceWiseFocalPersonContactList and MohaPhoneDirectoryList models with dummy data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        with transaction.atomic():
            provinces = Province.objects.all()

            for _ in range(20):
                province = fake.random_element(provinces)
                designation = fake.job()
                designation_ne = fake.job()
                govt_contact_person_name = fake.name()
                govt_contact_person_name_ne = fake.name()
                govt_contact_person_mobile = fake.phone_number()
                govt_contact_person_email = fake.email()
                province_focal_point_agency = fake.company()
                agency_contact_person_name = fake.name()
                agency_contact_person_name_ne = fake.name()
                agency_contact_person_mobile = fake.phone_number()
                agency_contact_person_email = fake.email()

                ProvinceWiseFocalPersonContactList.objects.create(
                    province=province,
                    designation=designation,
                    designation_ne=designation_ne,
                    govt_contact_person_name=govt_contact_person_name,
                    govt_contact_person_name_ne=govt_contact_person_name_ne,
                    govt_contact_person_mobile=govt_contact_person_mobile,
                    govt_contact_person_email=govt_contact_person_email,
                    province_focal_point_agency=province_focal_point_agency,
                    agency_contact_person_name=agency_contact_person_name,
                    agency_contact_person_name_ne=agency_contact_person_name_ne,
                    agency_contact_person_mobile=agency_contact_person_mobile,
                    agency_contact_person_email=agency_contact_person_email
                )

            for _ in range(20):
                division_section = fake.text()
                division_section_ne = fake.text()
                phone = fake.phone_number()
                mobile = fake.phone_number()
                email = fake.email()

                MohaPhoneDirectoryList.objects.create(
                    division_section=division_section,
                    division_section_ne=division_section_ne,
                    phone=phone,
                    mobile=mobile,
                    email=email
                )

        self.stdout.write(self.style.SUCCESS(
            'ProvinceWiseFocalPersonContactList and MohaPhoneDirectoryList models populated successfully.'))
