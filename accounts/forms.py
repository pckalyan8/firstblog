from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from accounts.models import AccountUser

class RegistrationForm(UserCreationForm):
    username    = forms.CharField(max_length=30 , help_text = 'Enter Username')
    email       = forms.EmailField(max_length=60 , help_text= 'Enter a Valid Email Address ')

    class Meta:
        model = AccountUser
        fields = ('username', 'email', 'password1', 'password2')
        


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label= 'password' , widget=forms.PasswordInput)

    class Meta():
        model   = AccountUser
        fields  = ('username','password')

    def clean(self):
        if self.is_valid:
            username    = self.cleaned_data['username']
            password    = self.cleaned_data['password']
            if not authenticate(username = username , password = password):
                raise forms.ValidationError('Invalid Login')

        
