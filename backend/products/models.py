from django.db import models
from services.models import PlantationService
# from django.contrib.auth.models import User

# Create your models here.

class PlantationImageVariation(models.Model):
    image = models.ImageField(upload_to="products/")
    
class PlantationProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    service = models.ForeignKey(PlantationService, on_delete=models.CASCADE, related_name="products")
    date = models.DateTimeField(auto_now_add=True)
    rent_price = models.FloatField(default=0.0)
    in_stock = models.BooleanField(default=True)
    stock = models.IntegerField(default=1)
    discount_percentage = models.IntegerField(default=0)
    tax_percentage = models.IntegerField(default=0)
    image = models.ImageField(upload_to="products/")
    variations = models.ManyToManyField(PlantationImageVariation, blank=True)
    shelf_number = models.CharField(max_length=50, default="R1")
    row_number = models.CharField(max_length=50, default="M2")

    class Meta:
        ordering = ("-date",)

    def buy(self, quantity): # when we buy we subtract from stock and email the admin that we dont have no more stock
        if self.stock - abs(quantity) < 0:
            # not enough stock
            return False
        
        self.stock -= abs(quantity)
        self.save()
        return True
        
    def save(self, *args, **kwargs):
        if self.stock <= 0:
            self.in_stock = False
        else:
            self.in_stock = True
        return super(PlantationProduct, self).save(args, kwargs)

    def add_stock(self, quantity):
        self.stock += quantity

    def __str__(self):
        return self.name