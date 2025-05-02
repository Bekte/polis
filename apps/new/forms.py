from django import forms
from .models import Registartion


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registartion
        fields = ['name', 'surname', 'email','about_you']

