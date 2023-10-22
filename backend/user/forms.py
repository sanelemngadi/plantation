# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import PlantationUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = PlantationUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 'as_admin')

        widgets = {
            "as_admin": forms.TextInput(attrs={"placeholder": "please enter your employement id"})
        }
