from django.core import validators
from django import forms
from .models import *


class Specialization_Form(forms.ModelForm):
    class Meta:
        model = Specialization
        fields = ["specialization_type"]
        widgets = {
            "specialization_type": forms.Select(
                attrs={"class": "form-select bg-dark text-light"}
            ),
        }


class Organization_Form(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ["name", "type", "specializations"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control bg-dark text-light"}),
            "type": forms.Select(attrs={"class": "form-control bg-dark text-light"}),
            "specializations": forms.SelectMultiple(
                attrs={"class": "form-control bg-dark text-light"}
            ),
        }


class Degree_Form(forms.ModelForm):
    class Meta:
        model = Degree
        fields = ["name"]
        widgets = {
            "name": forms.Select(attrs={"class": "form-control bg-dark text-light"})
        }


class Doctor_Form(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            "doctor_id",
            "first_name",
            "middle_name",
            "last_name",
            "image",
            "dob",
            "gender",
            "address",
            "degrees",
            "specialization",
            "organization_id",
            "phone_number",
        ]

        widgets = {
            "doctor_id": forms.TextInput(
                attrs={"class": "form-control bg-dark text-light"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control bg-dark text-light"}
            ),
            "middle_name": forms.TextInput(
                attrs={"class": "form-control bg-dark text-light"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control bg-dark text-light"}
            ),
            "image": forms.ClearableFileInput(
                attrs={"class": "form-control bg-dark text-light"}
            ),
            "dob": forms.DateInput(
                attrs={"type": "date", "class": "form-control bg-dark text-light"}
            ),
            "gender": forms.Select(attrs={"class": "form-select bg-dark text-light"}),
            "address": forms.Textarea(
                attrs={"rows": 3, "class": "form-control bg-dark text-light"}
            ),
            "degrees": forms.CheckboxSelectMultiple(
                attrs={"class": "list-unstyled bg-dark text-light"}
            ),
            "specialization": forms.Select(
                attrs={"class": "form-select bg-dark text-light"}
            ),
            "organization_id": forms.Select(
                attrs={"class": "form-select bg-dark text-light"}
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "pattern": "[0-9]{10}",
                    "title": "Please enter a 10-digit phone number",
                    "class": "form-control bg-dark text-light",
                }
            ),
        }
