from django.db import models
from orders.models import PlantationAddress
from products.models import PlantationProduct
# Create your models here.\\    

class PlantationSupplier(models.Model):
    street = models.CharField(max_length=200)
    provice = models.CharField(max_length=200)
    company_name = models.CharField(max_length=50)
    telephone = models.CharField(max_length=12)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.company_name
    

class PlantationProductInfo(models.Model):
    product = models.ForeignKey(PlantationProduct, on_delete=models.PROTECT)
    items_ordered = models.IntegerField(default=0)
    items_recieved = models.IntegerField(default=0)
    items_broken = models.IntegerField(default=0)
    item_price = models.FloatField(default=0.0)
    supplier = models.ForeignKey(PlantationSupplier, on_delete=models.PROTECT)

    def __str__(self):
        return self.product.name

class PlantationSupplierOrder(models.Model):
    products = models.ManyToManyField(PlantationProductInfo, blank=True)
    supplier = models.ForeignKey(PlantationSupplier, on_delete=models.PROTECT, related_name="orders")
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order No. {str(self.pk)}"