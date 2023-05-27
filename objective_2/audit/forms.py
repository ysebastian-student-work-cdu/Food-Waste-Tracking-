﻿from django import forms
from .models import *


# Django's ModelForm♦
class DonationForm(forms.ModelForm):
    # model attributes (userID, orgID, amount)
    class Meta:
        model = Donate
        # The fields to be included in the form
        fields = ['orgID', 'amount']

        # The exclude statement can replace fields. Every field will be displayed except those,
        # defined in exclude
        # exclude = []

        # Updates the names of the labels in the form on the webpage
        #labels = {
        #    'address': 'Postal Address',
        #    'state_province': 'State or Province'
        #}
class recipe(forms.ModelForm):
    class Meta:
        model = FoodForm
        fields = ('nameofItem1','quantity1','nameofItem2','quantity2','nameofItem3','quantity3')