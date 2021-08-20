from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from .models import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
class projectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title','description','projectscreenshot','projecturl']

class RateForm(forms.ModelForm):
    # text = forms.CharField(widget=forms.Textarea())
    # rate = forms.ChoiceField(choices=RATE_CHOICES,widget=forms.Select(),required=True)

    class Meta:
        model = Revieww
        fields = ['text','design','usability','content']