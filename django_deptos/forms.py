from typing import Any
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'box',
        'id':'name',
        'placeholder': 'Ingresa tu nombre de usuario',
    }))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={
        'class': 'box',
        'id':'password',
        'placeholder': 'Ingresa tu contraseña',
    }))
    correo = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'box',
        'id':'correo',
        'placeholder':'example@gmail.com'
    }))
    telefono = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'box',
        'id':'phone',
        'placeholder':'12345678'
    }))
    localidad = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={
        'class':'box',
        'id':'localidad',
        'placeholder':'Oberá'
    }))

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        
        if not telefono.isdigit():
            raise forms.ValidationError('El número de teléfono solo puede contener números.')
        return telefono