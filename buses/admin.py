from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin
from .models import BusStation,Timings

@admin.register(BusStation)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')

admin.site.register(Timings)