from django import forms

class RegisterForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'box',
        'id':'name',
        'placeholder': 'Nombre',
    })),
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={
        'class': 'box',
        'id':'password',
    })),
    correo = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'box',
        'id':'correo',
        'placeholder':'example@gmail.com'
    })),
    telefono = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={
        'class': 'box',
        'id':'phone',
        'placeholder':'12345678'
    })),
    localidad = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={
        'class':'box',
        'id':'localidad',
        'placeholder':'Oberá'
    })), 