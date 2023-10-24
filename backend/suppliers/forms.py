from django import forms 
from suppliers.models import PlantationSupplier, PlantationProductInfo

class PlantationSupplierCreateForm(forms.ModelForm):
    class Meta:
        model = PlantationSupplier
        fields = "__all__"

class PlantationStockingForm(forms.ModelForm):
    class Meta:
        model = PlantationProductInfo
        fields = "__all__"