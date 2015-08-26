from pkg_resources import resource_filename
from django.db.migrations.operations import RunPython

from .import_data import import_data


class LoadCountryData(RunPython):

    def __init__(self, country_code, **kwargs):
        self.country_code = country_code
        super(LoadCountryData, self).__init__(self.load_country_data, **kwargs)

    def load_country_data(self, apps, schema_editor):
        Admin = apps.get_model('local', 'Admin')
        Location = apps.get_model('local', 'Location')
        path = resource_filename(__name__, self.country_code + '.txt')
        import_data(path, Admin, Location)
