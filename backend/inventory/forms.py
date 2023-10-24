from django import forms
from inventory.models import PlantationWarehouseRow, PlantationWareHouseColumn, PlantationWareHouse

class PlantationRowForm(forms.ModelForm):
    class Meta:
        model = PlantationWarehouseRow
        fields = "__all__"

class PlantationShelfForm(forms.ModelForm):
    class Meta:
        model = PlantationWareHouseColumn
        fields = "__all__"

class PlantationWareHouseForm(forms.ModelForm):
    class Meta:
        model = PlantationWareHouse
        fields = "__all__"