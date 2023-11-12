from django.core import validators
from django import forms
from .models import *

class Specialization_Form(forms.ModelForm):
    class Meta:
        model=Specialization
        fields=['specialization_type']
        widgets = {
            'specialization_type': forms.Select(attrs={'class': 'form-select bg-dark text-light'}),
        }

class Organization_Form(forms.ModelForm):
    class Meta:
        model=Organization
        fields=['name','type','specializations']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-dark text-light'}),
            'type': forms.Select(attrs={'class': 'form-control bg-dark text-light'}),
            'specializations': forms.SelectMultiple(attrs={'class': 'form-control bg-dark text-light'}),
        }