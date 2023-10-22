from django import forms
from appointments.models import PlantationAppointmentsModel

class PlantationAppointmentForm(forms.ModelForm):
    class Meta:
        model = PlantationAppointmentsModel
        fields = "__all__"

        exclude = ("user", "appointment_done", "accepted", "reviewed", "confirmed")

        widgets = {
            "date": forms.DateInput(attrs={"type": "date"})
        }