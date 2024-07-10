from django import forms
from .models import Person

class UserForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['user_number', 'first_name', 'last_name', 'email', 'field_of_profession', 'salaray']
        labels = {
            'user_number': 'User Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'field_of_profession': 'Field of Profession',
            'salaray': 'Basic Salary'
        }
        widgets = {
            'user_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'field_of_profession': forms.TextInput(attrs={'class': 'form-control'}),
            'salaray': forms.NumberInput(attrs={'class': 'form-control'}),
        }
