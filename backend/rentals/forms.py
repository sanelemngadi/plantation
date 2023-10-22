from django import forms
from rentals.models import PlantationRentalModel

class PlantationRentalForm(forms.ModelForm):
    class Meta:
        model = PlantationRentalModel
        fields = "__all__"

        exclude = ("user", "status", "returned", "collected", "paid")

        widgets = {
            "date_from": forms.DateInput(attrs={"type": "date"}),
            "date_to": forms.DateInput(attrs={"type": "date"}),
            "reason": forms.Textarea(attrs={"type": "textarea"}),
        }
