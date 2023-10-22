from django.db import models
# from django.contrib.auth.models import User
from main.models import PlantationProduct
from user.models import PlantationUser

# Create your models here.
class PlantationAddress(models.Model):
    street_number = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    street_type = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    zip_code = models.IntegerField()

class PlantationCardInformation(models.Model):
    CHOICES = (("jan", "Jan"), ("feb", "Feb"), ("mar", "Mar"), ("apr", "Apr"), ("may", "May"),
               ("jun", "Jun"), ("jul", "Jul"), ("aug", "Aug"), ("sep", "Sep"), ("oct", "Oct"), 
               ("nov", "Nov"), ("dec", "Dec"))
    card_number = models.IntegerField()
    cvc = models.IntegerField()
    expiry_year = models.IntegerField(default=2023)
    expiry_month = models.CharField(max_length=4, default="Jan")

class PlantationOrderModel(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(PlantationProduct)
    user = models.ForeignKey(PlantationUser, on_delete=models.CASCADE, related_name="orders")
    paid = models.BooleanField(default=False) #if it is paid it becomes an order otherwise it stays in cart
    quantity = models.IntegerField(default=1)
    cellphone = models.CharField(max_length=11, default="031253551")
    address = models.ForeignKey(PlantationAddress, on_delete=models.CASCADE)
    card_information = models.ForeignKey(PlantationCardInformation, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, default="name@company.com")


    def add_products(self, products):
        if not self.pk:
            pass

        # self.products.set(products)
