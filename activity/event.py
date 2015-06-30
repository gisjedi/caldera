
import random
from datetime import timedelta

import arrow
from django.contrib.gis.geos import Point

from activity.models import PointStream


class Event(object):
    def __init__(self, north=90, south=-90, east=180, west=-180):
        self.north = north
        self.south = south
        self.east = east
        self.west = west

    def generate(self, count, start, end=None, load=None):
        """Generate the request number of features with event times randomly distributed across range

        :param count:
        :param start:
        :param end:
        :param load:
        :return:
        """
        if load is None:
            load = arrow.utcnow().datetime

        if end is None:
            end = arrow.utcnow().datetime

        fires = []
        for i in range(count):
            fire = PointStream()
            fire.event_date = self.random_date(start, end)
            fire.intensity = random.randrange(0, 5000)
            fire.load_date = load
            coordinates = self.get_location()
            fire.geom = Point(coordinates[0], coordinates[1])
            fires.append(fire)

        PointStream.objects.bulk_create(fires)

    def get_location(self):
        """Generate a random location between the given coordinates

        :return: tuple of x, y coordinates (lon, lat)
        """
        return (random.uniform(self.west, self.east),
                random.uniform(self.south, self.north))

    @staticmethod
    def random_date(start, end):
        """Generate a random datetime between two datetime objects.
        """
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = random.randrange(int_delta)
        return start + timedelta(seconds=random_second)
