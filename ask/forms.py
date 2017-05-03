# encoding=utf8
from django.forms import ModelForm
from django import forms
from ask.models import User


class RegistrationForm(ModelForm):
    repeat_password = forms.CharField(label='Repeat password')

    class Meta:
        model = User
        fields = '__all__'