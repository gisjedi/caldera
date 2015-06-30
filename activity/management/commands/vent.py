import argparse
import logging
import arrow

from django.core.management.base import BaseCommand
from activity.event import Event

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Generates a specified number of records within given time range'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="Count of records to generate within given time range.")
        parser.add_argument('start', type=self.valid_date, help="Start range in ISO 8601 format (2015-01-01T00:00:00Z)")
        parser.add_argument('end', type=self.valid_date, help="End range in ISO 8601 format (2015-01-01T00:00:00Z)")

    def handle(self, *args, **options):
        count = options['count']
        start = options['start']
        end = options['end']

        event = Event()
        logger.info('Creating %s events between %s and %s...' % (count, start, end))
        event.generate(count, start, end)
        logger.info('Completed.')

    @staticmethod
    def valid_date(date_str):
        try:
            return arrow.get(date_str).datetime
        except ValueError:
            msg = "Not a valid date: '%s'." % date_str
            raise argparse.ArgumentTypeError(msg)

