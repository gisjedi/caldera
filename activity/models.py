from django.contrib.gis.db import models


class PointStream(models.Model):
    id = models.AutoField(primary_key=True)
    event_date = models.DateTimeField(db_index=True)
    load_date = models.DateTimeField(db_index=True)
    intensity = models.FloatField()
    geom = models.PointField(srid=4326)

    objects = models.GeoManager()

    class Meta:
        db_table = 'point_stream'