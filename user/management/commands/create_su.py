from django.core.management.base import BaseCommand
from user.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        email = 'admin@todo.com'
        password = 'admin'
        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(email=email, password=password)
