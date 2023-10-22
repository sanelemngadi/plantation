from django import forms
from main.models import PlantationProduct, PlantationService

class PlantationProductForm(forms.ModelForm):
    class Meta:
        model = PlantationProduct
        fields = "__all__"

        exclude = ("service", )

class PlantationServiceForm(forms.ModelForm):
    class Meta:
        model = PlantationService
        fields = "__all__"