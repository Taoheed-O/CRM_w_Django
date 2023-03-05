from django import forms
from .models import Lead
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

# class LeadForm(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     age = forms.IntegerField(min_value=15)


User =  get_user_model()


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'email',
            'location',
            'about',
            'agent',
        )


class CustomerForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username",)
        fields_classes = {
            "username": UsernameField
        }