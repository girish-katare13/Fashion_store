from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs= {"class":"form-control", "placeholder" : "Pls Enter Your Email"}))
    username = forms.CharField(widget=forms.TextInput(attrs= {"class":"form-control", "placeholder" : "Username"}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs= {"class":"form-control", "placeholder" : "Password"}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs= {"class":"form-control", "placeholder" : "Confirm_Password"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')