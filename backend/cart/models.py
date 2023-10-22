from django.db import models
from user.models import PlantationUser
from main.models import PlantationProduct

# Create your models here.

class PlantationProductDetails(models.Model):
    product = models.ForeignKey(PlantationProduct, on_delete=models.PROTECT)
    quantity = models.IntegerField()

    def increment(self):
        self.quantity += 1
        self.save()

    def define(self, number: int):
        self.quantity = number
        self.save()


class PlantationCartModel(models.Model):
    user = models.ForeignKey(PlantationUser, on_delete=models.CASCADE, related_name="carts")
    items = models.ManyToManyField(PlantationProductDetails, blank=True)
    total_items = models.IntegerField(default=0, blank=True, null=True)
    total_price = models.FloatField(default=0.0, blank=True, null=True)

    def __str__(self):
        return self.user.first_name + "' cart"
    
    def get_net_total(self):
        return self.total_price - self.get_total_discount()
    
    def get_grand_total(self):
        return self.get_net_total() + self.get_total_tax()
    
    def get_total_price(self):
        total_price = 0
        for item in self.items.all():
            price = item.product.price
            count = item.quantity
            total_price += (count * price)
        return total_price
    
    def get_total_items(self):
        total_items = 0
        for item in self.items.all():
            count = item.quantity
            total_items += count
        return total_items
    
    def get_total_tax(self):
        total_tax = 0
        for item in self.items.all():
            count = item.quantity
            price = item.product.price
            tax_perc = item.product.tax_percentage
            tax = (count * price) * (tax_perc / 100)
            total_tax += tax
        return total_tax
    
    def get_total_discount(self):
        total_discount = 0
        for item in self.items.all():
            count = item.quantity
            price = item.product.price
            discount_perc = item.product.discount_percentage
            discount = (count * price) * (discount_perc / 100)
            total_discount += discount
        return total_discount

    
    def save(self, *args, **kwargs):
        if not self.pk:
            # If the instance doesn't have a primary key (i.e., it's not saved to the database yet), save it to generate one.
            super(PlantationCartModel, self).save(*args, **kwargs)


        self.total_price = self.get_total_price()
        self.total_items = self.get_total_items()

        return super(PlantationCartModel, self).save(args, kwargs)
    