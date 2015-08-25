from django.contrib import admin
from local import models


class AdminAdmin(admin.ModelAdmin):
    list_display = ('code', 'group', 'name',)
    list_filter = ('group',)
admin.site.register(models.Admin, AdminAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'place_name',
        'postal_code',
        'admin1',
        'admin2',
        'admin3',
        'country_code',
        'location',
    )
    list_filter = ('country_code', 'admin1', 'admin2', 'admin3',)
    search_fields = ('postal_code', 'place_name', )

admin.site.register(models.Location, LocationAdmin)
