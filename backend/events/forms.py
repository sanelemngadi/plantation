from django import forms
from events.models import PlantationEventModel

class PlantationEventForm(forms.ModelForm):
    class Meta:
        model = PlantationEventModel
        fields = '__all__'
        exclude = ("attendants", "host")

        widgets = {
            "date": forms.DateInput(attrs={"type": "date"})
        }