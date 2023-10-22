from django.db import models
# from django.contrib.auth.models import User
from user.models import PlantationUser

# Create your models here.

class PlantationAppointmentsModel(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    appointment_done = models.BooleanField(default=False)
    user = models.ForeignKey(PlantationUser, on_delete=models.CASCADE , related_name="appointments")
    accepted = models.BooleanField(default=False)
    reviewed = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    location = models.CharField(max_length=255, default="Cape town offices")