# Utilisateur/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from commondatab.models import ZzUsers

class InscriptionForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = ZzUsers
        fields = ['email', 'pseudo', 'nom', 'prenom', 'birthday', 'bio', 'sex', 'plage', 'astre', 'religion', 'longitude', 'latitude', 'city', 'country', 'hobby', 'pref']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class ConnexionForm(AuthenticationForm):
    username = forms.CharField(label='Email', max_length=255)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
