from django.core.management.base import BaseCommand
from ...test.factories import AddressFactory


class Command(BaseCommand):
    help = "generates fake users to list in the application"

    def add_arguments(self, parser):
        parser.add_argument("n_of_entries", type=int)

    def handle(self, *args, **options):
        AddressFactory.create_batch(options["n_of_entries"])

