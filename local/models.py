from django.contrib.gis.db import models
from django.contrib.gis.measure import D

ACCURACY_CHOICES = (
    (1, 'Estimated'),
    (2, ''),
    (3, 'Alternate Name'),
    (4, 'Name from GeoNames DB'),
    (5, ''),
    (6, 'Centroid'),
)


class Admin(models.Model):
    group = models.IntegerField()
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100, blank=True)

    class Meta:
        unique_together = (
            ('group', 'code',)
        )

    def __unicode__(self):
        return self.name


class Location(models.Model):
    country_code = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=10)
    place_name = models.CharField(max_length=180)
    admin1 = models.ForeignKey('Admin', blank=True, null=True,
                               limit_choices_to={'group': 1},
                               related_name='admin1_set')
    admin2 = models.ForeignKey('Admin', blank=True, null=True,
                               limit_choices_to={'group': 2},
                               related_name='admin2_set')
    admin3 = models.ForeignKey('Admin', blank=True, null=True,
                               limit_choices_to={'group': 3},
                               related_name='admin3_set')
    location = models.PointField()
    accuracy = models.PositiveIntegerField(choices=ACCURACY_CHOICES,
                                           null=True, blank=True)

    objects = models.GeoManager()

    def __unicode__(self):
        return u'[%s] %s' % (self.postal_code, self.place_name,)

    def surrounding_suburbs(self, distance, unit='km'):
        return Location.objects.filter(
            location__distance_lte=(self.location, D(**{unit: distance}))
        )
