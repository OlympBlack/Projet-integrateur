from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CompteUtilisateur(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = { 
            'username': forms.TextInput(attrs={'class': 'form-control border-danger'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border-danger'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control border-danger'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control border-danger'}),
        }