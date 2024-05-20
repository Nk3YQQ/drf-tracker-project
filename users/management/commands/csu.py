import os

from django.core.management import BaseCommand
from dotenv import load_dotenv

from users.models import User

load_dotenv()


class Command(BaseCommand):
    def handle(self, *args, **options):
        password = os.getenv("ADMIN_PASSWORD")

        superuser = User(
            first_name=os.getenv("ADMIN_NAME"),
            last_name=os.getenv("ADMIN_SURNAME"),
            email=os.getenv("ADMIN_EMAIL"),
            is_staff=True,
            is_superuser=True,
        )

        superuser.set_password(password)
        superuser.save()
