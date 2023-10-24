from django.db import models
from user.models import PlantationUser
from events.models import PlantationEventModel

# Create your models here.
class PlantationNotificationsModel(models.Model):
    user = models.ForeignKey(PlantationUser, on_delete=models.CASCADE, related_name="notifications")
    event = models.ForeignKey(PlantationEventModel, on_delete=models.PROTECT)
    viewed = models.BooleanField(default=False)
    rsvped = models.BooleanField(default=False)
    attended = models.BooleanField(default=False)
    bought_vip = models.BooleanField(default=True)

    qr_image = models.ImageField(upload_to="images/", max_length=800, null=True, blank=True)

    def __str__(self):
        return f"notification for: {self.user.get_name()}"

# class PlantationSubscribers(models.Model):
#     subscribers = models.ManyToManyField(PlantationUser, blank=True)