from django import forms
from .models import *
from django.conf import settings
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class FarmerForm(forms.ModelForm):
    phone_number = forms.CharField(widget=PhoneNumberPrefixWidget(),required=False, initial='+91')

    class Meta(object):
        model = Farmer
        fields = '__all__'