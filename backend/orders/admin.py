from django.contrib import admin
from orders.models import PlantationOrderModel, PlantationCardInformation, PlantationAddress

# Register your models here.

admin.site.register(PlantationOrderModel)
admin.site.register(PlantationCardInformation)
admin.site.register(PlantationAddress)