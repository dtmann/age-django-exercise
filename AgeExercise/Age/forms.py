from django import forms
from . import models
from .models import Person
from django.forms import ModelForm

class NewPersonForm(ModelForm):
    class Meta:
        model = models.Person
        fields = ['name', 'dob']