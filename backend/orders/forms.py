from django import forms
from orders.models import PlantationOrderModel, PlantationCardInformation, PlantationAddress

class PlantationOrderForm(forms.ModelForm):
    class Meta:
        model = PlantationOrderModel
        fields = "__all__"

        exclude = ("user", "paid", "products", "quantity", "address", "card_information")


class PlantationCardInformationForm(forms.ModelForm):
    class Meta:
        model = PlantationCardInformation
        fields = "__all__"


class PlantationAddressForm(forms.ModelForm):
    class Meta:
        model = PlantationAddress
        fields = "__all__"