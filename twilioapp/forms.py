from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import OTPVerification


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class OTPForm(forms.ModelForm):
    otp = forms.CharField(label='One-time Password (OTP)', required=True)
    
    class Meta:
        model = OTPVerification
        fields = ['otp']