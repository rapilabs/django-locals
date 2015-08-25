from local import models
from django import template

register = template.Library()


@register.filter
def postcode_to_suburb(postcode):
    return ', '.join([
        location for location in
        models.Location.objects.filter(
            postal_code=postcode
        ).values_list('place_name', flat=True)
    ])
