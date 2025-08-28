from django.contrib import admin
from .models import Podsh
from .models import City

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'country', 'region', 'okrug']
    list_filter = ['country', 'region', 'okrug']
    search_fields = ['city', 'country']

@admin.register(Podsh)
class PodshAdmin(admin.ModelAdmin):
    list_display = ['ID', 'POLN', 'FIRMA', 'GOST', 'STEEL']
    list_filter = ['FIRMA', 'GOST']
    search_fields = ['POLN', 'SLITN', 'OSNOVA', 'GOST', 'STEEL']
    readonly_fields = ['ID']  # если ID автоинкрементный

from django.contrib import admin
from .models import Price

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    # Указывайте только те поля, которые реально есть в модели Price
    list_display = [ 'bearing',  'kolwo', 'cena', 'sales', 'reserv']
    list_filter = ['reserv', 'bearing']  # Только поля, которые существуют
    search_fields = ['bearing', 'sales']