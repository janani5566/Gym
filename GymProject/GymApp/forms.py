from django import forms
from .models import Register
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):

    class Meta:
        model = Register
        fields = [
            'name',
            'age',
            'address',
            'phone',
            'goal',
            'gender',
            ]
