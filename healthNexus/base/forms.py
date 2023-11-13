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

    def clean_doctor_id(self):
        doctor_id = self.cleaned_data["doctor_id"]
        if not doctor_id.isdigit() or len(doctor_id) != 16:
            raise forms.ValidationError(
                "Doctor ID should be exactly 16 digits and contain only digits."
            )
        return doctor_id

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise forms.ValidationError(
                "Phone number should be exactly 10 digits and contain only digits."
            )
        return phone_number


class Organisation_Staff_Form(forms.ModelForm):
    class Meta:
        model = Organization_Staff
        fields = [
            "staff_id",
            "first_name",
            "middle_name",
            "last_name",
            "designation",
            "image",
            "gender",
            "dob",
            "address",
            "organization_id",
            "phone_number",
        ]
        widgets = {
            "staff_id": forms.TextInput(
                attrs={
                    "class": "form-control bg-dark text-light",
                    "placeholder": "Staff ID",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control bg-dark text-light",
                    "placeholder": "First Name",
                }
            ),
            "middle_name": forms.TextInput(
                attrs={
                    "class": "form-control bg-dark text-light",
                    "placeholder": "Middle Name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control bg-dark text-light",
                    "placeholder": "Last Name",
                }
            ),
            "designation": forms.Select(
                attrs={"class": "form-select bg-dark text-light"}
            ),
            "image": forms.ClearableFileInput(
                attrs={"class": "form-control bg-dark text-light"}
            ),
            "gender": forms.Select(attrs={"class": "form-select bg-dark text-light"}),
            "dob": forms.DateInput(
                attrs={"class": "form-control bg-dark text-light", "type": "date"}
            ),
            "address": forms.Textarea(
                attrs={
                    "class": "form-control bg-dark text-light",
                    "placeholder": "Address",
                }
            ),
            "organization_id": forms.Select(
                attrs={"class": "form-select bg-dark text-light"}
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control bg-dark text-light",
                    "placeholder": "Phone Number",
                }
            ),
        }

    def clean_staff_id(self):
        staff_id = self.cleaned_data["staff_id"]
        if not staff_id.isdigit() or len(staff_id) != 16:
            raise forms.ValidationError(
                "Staff Id should be exactly 16 digits and contain only digits."
            )
        return staff_id

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise forms.ValidationError(
                "Phone number should be exactly 10 digits and contain only digits."
            )
        return phone_number


class Patient_Form(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "patient_id",
            "first_name",
            "middle_name",
            "last_name",
            "image",
            "gender",
            "dob",
            "address",
            "phone_number",
        ]
        widgets = {
            "patient_id": forms.TextInput(
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
            "gender": forms.Select(attrs={"class": "form-control bg-dark text-light"}),
            "dob": forms.DateInput(
                attrs={"class": "form-control bg-dark text-light", "type": "date"}
            ),
            "address": forms.Textarea(
                attrs={"class": "form-control bg-dark text-light"}
            ),
            "phone_number": forms.TextInput(
                attrs={"class": "form-control bg-dark text-light"}
            ),
        }

    def clean_patient_id(self):
        patient_id = self.cleaned_data["patient_id"]
        if not patient_id.isdigit() or len(patient_id) != 16:
            raise forms.ValidationError(
                "Patient Id should be exactly 16 digits and contain only digits."
            )
        return patient_id

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise forms.ValidationError(
                "Phone number should be exactly 10 digits and contain only digits."
            )
        return phone_number


class Patient_History_Form(forms.ModelForm):
    class Meta:
        model = Patient_History
        fields = [
            "patient_id",
            "doctor_id",
            "staff_id",
            "organization_id",
            "patient_report_pdf",
            "lab_reports_pdf",
        ]

        widgets = {
            "patient_id": forms.Select(
                attrs={"class": "form-select bg-dark text-light"}
            ),
            "doctor_id": forms.Select(
                attrs={"class": "form-select bg-dark text-light"}
            ),
            "staff_id": forms.SelectMultiple(
                attrs={"class": "form-select bg-dark text-light"}
            ),
            "organization_id": forms.Select(
                attrs={"class": "form-select bg-dark text-light"}
            ),
            "patient_report_pdf": forms.ClearableFileInput(
                attrs={"class": "form-control-file bg-dark text-light"}
            ),
            "lab_reports_pdf": forms.ClearableFileInput(
                attrs={"class": "form-control-file bg-dark text-light"}
            ),
        }
