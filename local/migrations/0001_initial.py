# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.IntegerField()),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_code', models.CharField(max_length=2)),
                ('postal_code', models.CharField(max_length=10)),
                ('place_name', models.CharField(max_length=180)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('accuracy', models.PositiveIntegerField(blank=True, null=True, choices=[(1, b'Estimated'), (2, b''), (3, b'Alternate Name'), (4, b'Name from GeoNames DB'), (5, b''), (6, b'Centroid')])),
                ('admin1', models.ForeignKey(related_name='admin1_set', blank=True, to='local.Admin', null=True)),
                ('admin2', models.ForeignKey(related_name='admin2_set', blank=True, to='local.Admin', null=True)),
                ('admin3', models.ForeignKey(related_name='admin3_set', blank=True, to='local.Admin', null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='admin',
            unique_together=set([('group', 'code')]),
        ),
    ]
