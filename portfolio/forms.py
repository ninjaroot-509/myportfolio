from django import forms
from .models import *


class ContactusForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = '__all__'
        