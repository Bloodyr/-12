from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Auto


class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['brand', 'model', 'gov_number']