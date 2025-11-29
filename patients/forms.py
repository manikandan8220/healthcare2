from django import forms
from .models import Patient, HealthRecord


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'contact', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }


class HealthForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ['heart_rate', 'blood_pressure', 'sugar_level', 'temperature']
        widgets = {
            'heart_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'blood_pressure': forms.TextInput(attrs={'class': 'form-control'}),
            'sugar_level': forms.NumberInput(attrs={'class': 'form-control'}),
            'temperature': forms.NumberInput(attrs={'class': 'form-control'}),
        }
