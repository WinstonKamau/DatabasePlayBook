from django.core.management.base import BaseCommand, CommandError
from logogram.users.create_table.create_table import create_user_table
from logogram.flashcards.create_table.create_table import (
    create_flashcards_table)


class Command(BaseCommand):
    help = ('Create tables on the application')

    def handle(self, *args, **options):
        try:
            create_user_table()
            create_flashcards_table()
        except Exception as error:
            raise CommandError(error)
        self.stdout.write(self.style.SUCCESS('Database Tables Created'))
