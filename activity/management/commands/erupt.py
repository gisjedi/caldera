import logging
import sys
import signal
from datetime import timedelta
from time import sleep
import arrow

from django.core.management.base import BaseCommand

from activity.event import Event

logger = logging.getLogger(__name__)

# Running will be true as long as the application should continue looping
running = True
# Dormant is used to detect a sleep state
dormant = True


def signal_handler(signal, frame):
    global running
    running = False
    logger.info('SIGINT detected. Ending after other processes complete...')
    if dormant:
        logger.info('Sleep detected. Terminating.')
        sys.exit(0)


class Command(BaseCommand):
    help = 'Generates a specified number of records at a specified second interval'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)
        parser.add_argument('interval', type=int)

    def handle(self, *args, **options):
        global dormant
        count = options['count']
        interval = options['interval']

        signal.signal(signal.SIGINT, signal_handler)

        while running:
            dormant = False
            event = Event()
            past = arrow.utcnow().datetime - timedelta(seconds=interval)
            now = arrow.utcnow().datetime

            logger.info('Creating %s events between %s and %s...' % (count, past, now))
            event.generate(count, past, now)
            dormant = True

            if running:
                # Sleep until the interval has elapsed
                logger.info('Sleeping %s seconds...' % interval)
                sleep(interval)

        logger.info('Complete.')

