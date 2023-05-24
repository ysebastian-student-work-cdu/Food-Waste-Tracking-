from django import forms
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
