# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PointStream',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('event_date', models.DateTimeField(db_index=True)),
                ('load_date', models.DateTimeField(db_index=True)),
                ('intensity', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'db_table': 'point_stream',
            },
        ),
    ]
