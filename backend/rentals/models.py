from django.db import models
from main.models import PlantationProduct
# from django.contrib.auth.models import User
from user.models import PlantationUser

# Create your models here.

class PlantationRentalModel(models.Model):
    STATUS_CHOICES = (
        ("pending", "pending"),
        ("overdue", "overdue"),
        ("time", "on time"),
    )
    # when we delete a rental we don't need to delete a product not even by a mistake
    product = models.ForeignKey(PlantationProduct, on_delete=models.PROTECT)
    user = models.ForeignKey(PlantationUser, on_delete=models.PROTECT, related_name="rentals")
    date_request = models.DateTimeField(auto_now_add=True)
    date_from = models.DateField()
    date_to = models.DateField()
    returned = models.BooleanField(default=False)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    paid = models.BooleanField(default=False)
    reason = models.CharField(max_length=255 ,default="To study")
    collected = models.BooleanField(default=False)
