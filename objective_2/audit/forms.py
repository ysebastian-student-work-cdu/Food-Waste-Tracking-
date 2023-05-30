from django import forms
from .models import *


# Django's ModelForm
class DonationForm(forms.ModelForm):

    # model attributes (userID, orgID, amount)
    class Meta:
        model = Donate
        # The fields to be included in the form
      
        fields = ('userID','orgID', 'amount', 'date')
        widgets = {
                       #'userID':forms.HiddenInput(), 
                       'date': forms.TextInput(attrs={'readonly': 'readonly'})
                  }


class DonationsForm(forms.Form):

    userID= forms.CharField(widget = forms.HiddenInput(), max_length=30)    # foreign key of userID in user table
    orgID= forms.CharField(max_length=30)# Foreigh  key of organisation id field
    amount = forms.DecimalField(max_digits=7, decimal_places=2) # Amount donated by the user (max is $9999999 for one donation)
    date = forms.DateField(widget = forms.HiddenInput())




        

class recipeForm(forms.ModelForm):
    class Meta:
        model = FoodForm
        fields = ('nameofItem1','quantity1','nameofItem2','quantity2','nameofItem3','quantity3')


class CreateWasteEntry(forms.ModelForm):
    class Meta:
        model = WasteEntries
        fields = ['userID', 'date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})

class WasteItemForm(forms.ModelForm):
    class Meta:
        model = WasteItems
        fields = ['itemDescription', 'quantity']