Installation
------------

`pip install git+git://github.com/funkybob/django-locals.git`

or in your requirements.txt:

`-e git+git://github.com/funkybob/django-locals.git#egg=local`

and in your settings.py add:

```python
INSTALLED_APPS = (
    # ...
    'local',
)
```

and apply the initial migration:

`./manage.py migrate local`

Initial Dataset
---------------

The initial location dataset may either be loaded via a management command:

`./manage.py load_geonames <path-to-dataset>`

or by creating a migration from the supplied data migration (eg with the AU dataset):

```python
from django.db import models, migrations
from local.operations import LoadCountryData


class Migration(migrations.Migration):

    dependencies = [
        # ... your dependencies here ...
        ('local', '0001_initial'),
    ]

    operations = [
        LoadCountryData('AU'),
    ]
```
