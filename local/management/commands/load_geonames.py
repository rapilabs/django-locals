from django.core.management.base import BaseCommand

from .models import Admin, Location
from .import_data import import_data


class Command(BaseCommand):
    args = '<GeoNames Dump File>'
    help = 'Load GeoNames Dump file'

    def handle(self, *args, **kwargs):
        import_data(args[0], Admin, Location)
