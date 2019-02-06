from django.core.management.base import BaseCommand, CommandError
from logogram.users.drop_table.drop_table import drop_user_table
from logogram.flashcards.drop_table.drop_table import drop_flashcards_table


class Command(BaseCommand):
    help = ('Drop tables on the application')

    def handle(self, *args, **options):
        try:
            drop_flashcards_table()
            drop_user_table()
        except Exception as error:
            raise CommandError(error)
        self.stdout.write(self.style.SUCCESS('Database Tables Dropped'))
