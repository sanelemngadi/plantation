from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class PlantationService(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="services/")

    class Meta:
        ordering = ("-date",)

    def __str__(self):
        return self.title