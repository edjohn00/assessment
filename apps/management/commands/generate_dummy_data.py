from factories import BloggerFactory
from django.core.management import BaseCommand
from django.db import transaction


@transaction.atomic
class Command(BaseCommand):
    help = "Generate dummy data"

    @transaction.atomic
    def generate_dummy_data(self):
        number_of_blogger = 23
        for _ in range(number_of_blogger):
            BloggerFactory()

    def handle(self, *args, **kwargs):
        self.generate_dummy_data()
        print("Dummy data generated")
