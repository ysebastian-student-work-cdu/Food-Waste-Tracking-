from django.db import models
from django.utils import timezone


class organisation(models.Model):
    name= models.CharField('Organisation Name', max_length=90)
    description= models.TextField(blank=True)
    type= models.CharField('Organisation Type', max_length=90)
    
    
    def __str__(self):
        return self.name
    
   
   
class User(models.Model):
    first_name= models.CharField('First Name', max_length=90)
    last_name= models.CharField('Last Name', max_length=90)
    id= models.CharField('User ID', max_length=30)
    password= models.CharField('Password', max_length=90)
    signup_date = models.DateTimeField(default=timezone.now)
    location = models.CharField('Location', max_length=120)
    email_address = models.EmailField('Email', max_length=90)
    
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class FoodRecipients(models.Model,WasteCollection):
    foodID= models.CharField('Food ID', max_length=30)
    foodEntryID= models.CharField('Food entry ID', max_length=30)
    quantity= models.CharField('Quantity of food', max_length=90)
    typeOfFood= models.CharField('Type of food i.e. Mexican, Chinese', max_length=90)
    RetrievedRecipie= models.CharField('Retrieved Recipie', max_length=90)
    
    
class WasteCollection(models.Model):
    wasteItemID= models.CharField('WasteItem ID', max_length=30)
    wasteEntryID= models.CharField('Waste entry ID', max_length=30)
    quantity= models.CharField('Quantity of waste', max_length=90)
    disposalmethod= models.CharField('Disposal method', max_length=90)
    donationID= models.CharField('Donation ID', max_length=90)
    organisation= models.ForeignKey(organisation, blank=True, null=True, on_delete=models.CASCADE)
    attendees= models.ManyToManyField(Users, blank=True)
    
    def __str__(self):
        return self.name
    
   

     
