from django.contrib.auth import authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import NumberInput, EmailInput, TextInput
from phonenumber_field.modelfields import PhoneNumberField

from .models import User


class AuthenticationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=254)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError(f'there is not {username} in my users')


class SignUpForm(UserCreationForm):
    name = forms.CharField(help_text='Required')
    surname = forms.CharField(help_text='Required')
    email = forms.EmailField(help_text='Required',
                             widget=EmailInput(attrs={'autocomplete': 'email'}))
    phone = forms.CharField(help_text='As you like', required=False)
    birth_date = forms.DateField(help_text='As you like', required=False,
                                 widget=NumberInput(attrs={'type': 'date'}))
    city = forms.CharField(help_text='As you like', required=False)
    image = forms.ImageField(help_text='As you like', required=False)

    class Meta:
        model = User
        fields = ('username', 'name', 'surname', "email", 'phone', 'birth_date', 'city', 'image')
