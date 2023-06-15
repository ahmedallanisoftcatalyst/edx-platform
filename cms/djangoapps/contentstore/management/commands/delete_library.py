"""
Management Command to delete a v1 library.
"""
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    Delete a MongoDB backed v1 library

    Example usage:
        $ ./manage.py cms delete_library '<library ID>'
    """

    help = 'Delete a MongoDB backed course'

    def add_arguments(self, parser):
        parser.add_argument(
            'library_key',
            help='ID of the library to delete.',
        )

    def handle(self, *args, **options):
        try:
            library_key = str(options['library_key'], 'utf8')
        # May already be decoded to unicode if coming in through tests, this is ok.
        except TypeError:
            library_key = str(options['library_key'])

        print(f'"****** In management command to delete library {library_key}')
