# mysite/accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Formateur, Formation, Etudiant, Registration,CustomUser
 
class CustomRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email', 'password','adress','numero','gender']

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
