from django import forms
from django.db import models
from django.contrib.auth import models as auth
from django.core.validators import MinLengthValidator, MinValueValidator
from django.utils.html import format_html

class WasteEntries(models.Model):
    wasteEntryID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(
        auth.User,
        on_delete=models.CASCADE,
        db_column='userID'
    )
    date = models.DateField()

    class Meta:
        verbose_name_plural = "Waste Entries"

    def __str__(self):
        return f"{self.wasteEntryID}. {self.userID} ({self.date})"

class WasteItems(models.Model):
    wasteItemID = models.AutoField(primary_key=True)
    wasteEntryID = models.ForeignKey(WasteEntries, on_delete=models.CASCADE)
    itemDescription = models.CharField(max_length=64)
    quantity = models.FloatField(
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name_plural = "Waste Items"

    def __str__(self):
        return f"{self.itemDescription}, {self.wasteEntryID.userID} ({self.wasteEntryID.date})"


class Organisation(models.Model):
    orgid = models.CharField('Organisation', primary_key=True, max_length = 30)    
    description= models.TextField(blank=True)
    orgtype = models.CharField('Organisation Type', null=True, max_length=90)
    
    
    def __str__(self):
        return self.orgid

class Donate(models.Model):
     userID= models.ForeignKey(auth.User, on_delete =models.CASCADE, db_column = 'userID')    # foreign key of userID in user table
     orgID= models.ForeignKey(Organisation, on_delete = models.CASCADE, db_column = 'orgid') # Foreigh  key of organisation id field
     amount = models.IntegerField('Amount(kg)') # Amount donated by the user (max is $9999999 for one donation)
     date = models.DateTimeField()
     def __str__(self):
        return str(self.userID)

# For getting the recipies from the waste produce 
class FoodForm(models.Model):
    nameofItem1 = models.CharField(max_length=100)
    quantity1 = models.IntegerField()
    nameofItem2 = models.CharField(max_length=100)
    quantity2 = models.IntegerField()
    nameofItem3 = models.CharField(max_length=100)
    quantity3 = models.IntegerField()
    
    def  __str__(self) -> str:
        return self.nameofItem1
    
class RecipesSaved(models.Model):
    Recipe=models.CharField(max_length=22200)
    
    def __str__(self):
        return self.Recipe  
    

