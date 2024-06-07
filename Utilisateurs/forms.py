from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

#form pour le formulaire d'inscription
class CompteUtilisateur(UserCreationForm):
    class Meta:
        models = User
        Fields = ['username', 'email', 'password', 'confirmepassword']
        widgets = { 
            'username': forms.TextInput(attrs={'class': 'form-control border-danger'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border-danger'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control border-danger'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control border-danger'}),
        }
