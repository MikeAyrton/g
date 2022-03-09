from dataclasses import field, fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# class RatingForm(forms.ModelForm):
#     star = forms.ModelChoiceField(
#         queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None)
    
#     class Meta:
#         model = Rating
#         fields = ["star"]

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class SentMessageForm(forms.ModelForm):
    class Meta:
        model=SendMessage
        fields='__all__'
