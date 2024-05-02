from django.core.management.base import BaseCommand
from federal.models import Province


class Command(BaseCommand):
    help = 'Populate Province with real province names of Nepal'

    PROVINCE_NAMES = [
        ('Province No. 1', 'प्रदेश नं. १'),
        ('Province No. 2', 'प्रदेश नं. २'),
        ('Bagmati Province', 'बागमती प्रदेश'),
        ('Gandaki Province', 'गण्डकी प्रदेश'),
        ('Lumbini Province', 'लुम्बिनी प्रदेश'),
        ('Karnali Province', 'कर्णाली प्रदेश'),
        ('Sudurpashchim Province', 'सुदूरपश्चिम प्रदेश'),
    ]

    def handle(self, *args, **kwargs):
        for province_name, province_name_ne in self.PROVINCE_NAMES:
            Province.objects.create(
                province_name=province_name,
                province_name_ne=province_name_ne,
                code=''  # TODO: Add code field to Province model
            )

        self.stdout.write(self.style.SUCCESS(
            'Provinces created successfully.'))
