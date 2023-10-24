from django.contrib import admin
from suppliers.models import PlantationProductInfo, PlantationSupplier, PlantationSupplierOrder

# Register your models here.

admin.site.register(PlantationProductInfo)
admin.site.register(PlantationSupplier)
admin.site.register(PlantationSupplierOrder)
