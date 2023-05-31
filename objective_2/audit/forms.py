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
                       'userID':forms.HiddenInput(), 
                  }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})





        

class recipeForm(forms.ModelForm):
    class Meta:
        model = FoodForm
        fields = ('nameofItem1','quantity1','nameofItem2','quantity2','nameofItem3','quantity3')


class CreateWasteEntry(forms.ModelForm):
    class Meta:
        model = WasteEntries
        fields = ['userID', 'date']
        widgets = {'userID':forms.HiddenInput()}


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})


class WasteItemForm(forms.ModelForm):
    class Meta:
        model = WasteItems
        fields = ['itemDescription', 'quantity']