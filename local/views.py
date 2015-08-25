import json

from django.db.models import Q
from django.http import HttpResponse

from local.models import Location


def search(request):
    qset = Location.objects.order_by('postal_code').values(
        'id',
        'postal_code',
        'place_name'
    ).distinct()
    obj_id = request.GET.get('id', None)
    if obj_id:
        qset = qset.filter(pk=obj_id)
    else:
        query = request.GET.get('query', None)
        if query:
            qset = qset.filter(
                Q(postal_code__startswith=query) | Q(place_name__icontains=query)
            )
        try:
            limit = int(request.GET['limit'])
        except (KeyError, ValueError):
            limit = None
        if limit:
            try:
                offset = int(request.GET.get('start', 0))
            except (KeyError, ValueError):
                offset = 0
            qset = qset[offset:offset+limit]
    return HttpResponse(json.dumps(tuple(qset)))
