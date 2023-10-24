from django import forms
from products.models import PlantationProduct

class PlantationProductForm(forms.ModelForm):
    class Meta:
        model = PlantationProduct
        fields = "__all__"

        exclude = ("service", )