from django import forms
from services.models import PlantationService

class PlantationServiceForm(forms.ModelForm):
    class Meta:
        model = PlantationService
        fields = "__all__"