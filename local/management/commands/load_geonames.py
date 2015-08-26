from django.core.management.base import BaseCommand

from local import models
from django import forms
import csv


class ImportForm(forms.ModelForm):
    class Meta:
        model = models.Location
        exclude = []

# Field names for GeoNames download format
field_names = [
    'country_code',
    'postal_code',
    'place_name',
    'admin_name1',
    'admin_code1',
    'admin_name2',
    'admin_code2',
    'admin_name3',
    'admin_code3',
    'lattitude',
    'longitude',
    'accuracy'
]


class Command(BaseCommand):
    args = '<GeoNames Dump File>'
    help = 'Load GeonNames Dump file'

    def handle(self, *args, **kwargs):
        fin = open(args[0], 'rb')
        xin = csv.DictReader(fin, delimiter='\t', fieldnames=field_names)

        for count, row in enumerate(xin):
            # Extract and find Admin 1, 2, 3
            if row['admin_code1']:
                rec, created = models.Admin.objects.get_or_create(
                    code=row['admin_code1'],
                    name=row['admin_name1'],
                    group=1
                )
                row['admin1'] = rec.id
            if row['admin_code2']:
                rec, created = models.Admin.objects.get_or_create(
                    code=row['admin_code2'],
                    name=row['admin_name2'],
                    group=2
                )
                row['admin2'] = rec.id
            if row['admin_code3']:
                rec, created = models.Admin.objects.get_or_create(
                    code=row['admin_code3'],
                    name=row['admin_name3'],
                    group=3
                )
                row['admin3'] = rec.id

            row['location'] = 'POINT(%(longitude)s %(lattitude)s)' % row
            form = ImportForm(row)
            if form.is_valid():
                form.save()
            else:
                print "[%s] Failed: %s\n" % (count, form.errors,)
        fin.close()
