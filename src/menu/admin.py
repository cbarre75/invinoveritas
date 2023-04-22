from django.contrib import admin

from .models import Vin

class VinAdmin(admin.ModelAdmin):
    list_display = ('nom', 'pays', 'region', 'millesime', 'producteur')
    search_fields = ['nom']


# Register your models here.
admin.site.register(Vin, VinAdmin)