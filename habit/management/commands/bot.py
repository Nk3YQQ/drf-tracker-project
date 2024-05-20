from django.core.management import BaseCommand

from habit.setup import main


class Command(BaseCommand):
    def handle(self, *args, **options):
        main()
