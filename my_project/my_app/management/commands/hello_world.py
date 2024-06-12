from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Logs 'Hello World'"

    def handle(self, *args, **options):
        try:
            self.log()

        except Exception as e:
            raise CommandError(f"Error: {str(e)}")

    def log(self):
        print("Hello World")
