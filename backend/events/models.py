from django.db import models
# from django.contrib.auth.models import User
from user.models import PlantationUser
# Create your models here.

class PlantationEventModel(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.TextField()
    vip_price = models.FloatField(default=0.0)
    general_price = models.FloatField(default=0.0)
    attandants = models.ManyToManyField(PlantationUser, related_name="events", blank=True)
    location = models.CharField(max_length=255, default="No location mentioned")
    host = models.ForeignKey(PlantationUser, on_delete=models.CASCADE, null=True, blank=True)
    duration_mins = models.IntegerField(default=10)
    time = models.CharField(max_length=30, default="10:00 AM")
    
    def __str__(self):
        return self.title


    