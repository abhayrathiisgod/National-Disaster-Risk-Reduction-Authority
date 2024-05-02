# federal/management/commands/populate_rest.py

from django.core.management.base import BaseCommand
from federal.models import Province, District, Municipality

nepal_provinces_districts = [
    ["Province No. 1", ["Bhojpur", "Dhankuta", "Ilam", "Jhapa", "Khotang", "Morang", "Okhaldhunga",
                        "Panchthar", "Sankhuwasabha", "Solukhumbu", "Sunsari", "Taplejung", "Terhathum", "Udayapur"]],
    ["Province No. 2", ["Bara", "Parsa", "Rautahat",
                        "Saptari", "Siraha", "Dhanusa", "Mahottari"]],
    ["Bagmati Province", ["Bhaktapur", "Chitwan", "Dhading", "Dolakha", "Kathmandu", "Kavrepalanchok",
                          "Lalitpur", "Makwanpur", "Nuwakot", "Ramechhap", "Rasuwa", "Sindhuli", "Sindhupalchok"]],
    ["Gandaki Province", ["Baglung", "Gorkha", "Kaski", "Lamjung", "Manang",
                          "Mustang", "Myagdi", "Nawalpur", "Parbat", "Syangja", "Tanahun"]],
    ["Lumbini Province", ["Arghakhanchi", "Gulmi", "Kapilvastu",
                          "Nawalparasi East", "Nawalparasi West", "Palpa", "Rupandehi"]],
    ["Karnali Province", ["Dailekh", "Dolpa", "Humla", "Jajarkot",
                          "Jumla", "Kalikot", "Mugu", "Salyan", "Surkhet"]],
    ["Sudurpashchim Province", ["Achham", "Baitadi", "Bajhang", "Bajura",
                                "Dadeldhura", "Darchula", "Doti", "Kailali", "Kanchanpur"]]
]


class Command(BaseCommand):
    help = "Populates the database with provinces, districts, and municipalities of Nepal."

    def handle(self, *args, **kwargs):
        for province_info in nepal_provinces_districts:
            province_name = province_info[0]
            districts = province_info[1]

            # Get or create the province
            province_obj, created = Province.objects.get_or_create(
                province_name=province_name,
                defaults={'province_name_ne': province_name}
            )

            # Iterate over the districts
            for district_name in districts:
                # Get or create the district
                district_obj, created = District.objects.get_or_create(
                    province=province_obj,
                    district_name=district_name,
                    defaults={'district_name_ne': district_name}
                )

                # Create municipalities for each district
                for i in range(1, 10):  # Assuming there are 10 municipalities in each district
                    municipality_name = f"{district_name} Municipality {i}"
                    municipality_name_ne = f"{
                        district_name} म्युनिसिपालिटी {i}"

                    # Create municipality
                    Municipality.objects.create(
                        province=province_obj,
                        district=district_obj,
                        municipality_name=municipality_name,
                        municipality_name_ne=municipality_name_ne
                    )

        self.stdout.write(self.style.SUCCESS(
            'Successfully populated the database with Nepali regions.'))
