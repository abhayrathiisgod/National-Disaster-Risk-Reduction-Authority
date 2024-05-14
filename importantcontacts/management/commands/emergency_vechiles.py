from django.db import transaction
from django.core.management.base import BaseCommand
from faker import Faker
from federal.models import Province, District, Municipality
from importantcontacts.models import EmergencyVehicle


class Command(BaseCommand):
    help = 'Populate EmergencyVehicle model with dummy data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        with transaction.atomic():
            for _ in range(10):  # Adjust the range as needed
                vehicle_type = fake.random_element(
                    elements=['Ambulance', 'Fire_truck', 'Police_vehicle']
                )
                ownership = fake.company()
                ownership_ne = fake.company()
                vehicle_no = fake.license_plate()
                vehicle_no_ne = fake.license_plate()
                driver_name = fake.name()
                driver_name_ne = fake.name()
                contact = fake.phone_number()
                alt_contact = fake.phone_number()
                condition = fake.text(max_nb_chars=200)
                province = Province.objects.order_by('?').first()
                district = District.objects.order_by('?').first()
                municipality = Municipality.objects.order_by(
                    '?').first()

                EmergencyVehicle.objects.create(
                    vehicle_type=vehicle_type,
                    ownership=ownership,
                    ownership_ne=ownership_ne,
                    vechicle_no=vehicle_no,
                    vechicle_no_ne=vehicle_no_ne,
                    driver_name=driver_name,
                    driver_name_ne=driver_name_ne,
                    contact=contact,
                    alt_contact=alt_contact,
                    condition=condition,
                    province=province,
                    district=district,
                    municipality=municipality
                )

        self.stdout.write(self.style.SUCCESS(
            'EmergencyVehicle model populated successfully.'))
