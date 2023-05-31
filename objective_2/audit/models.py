from django import forms
from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from django.utils.html import format_html

class UserRoles(models.Model):
    roleID = models.IntegerField(primary_key=True)
    roleName = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "User Roles"

    def __str__(self):
        return self.roleName

class Users(models.Model):
    userID = models.AutoField(primary_key=True)
    roleID = models.ForeignKey(UserRoles, on_delete=models.CASCADE)
    username = models.CharField(
        max_length=32,
        validators=[MinLengthValidator(5)]
    )
    password = models.CharField(
        max_length=64,
        validators=[MinLengthValidator(8)]
    )
    nickname = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return str(self.username)

class WasteEntries(models.Model):
    wasteEntryID = models.AutoField(primary_key=True)
    userID = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        db_column='userID'
    )
    date = models.DateField()

    class Meta:
        verbose_name_plural = "Waste Entries"

    def __str__(self):
        return f"{self.wasteEntryID}. {self.userID.username} ({self.date})"

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
        return f"{self.itemDescription}, {self.wasteEntryID.userID.username} ({self.wasteEntryID.date})"


class Organisation(models.Model):
    orgid = models.CharField('Organisation', primary_key=True, max_length = 30)    
    description= models.TextField(blank=True)
    orgtype = models.CharField('Organisation Type', null=True, max_length=90)
    
    
    def __str__(self):
        return self.orgid

class Donate(models.Model):
     userID= models.ForeignKey(Users, on_delete =models.CASCADE, db_column = 'userID')    # foreign key of userID in user table
     orgID= models.ForeignKey(Organisation, on_delete = models.CASCADE, db_column = 'orgid') # Foreigh  key of organisation id field
     amount = models.IntegerField('Amount(kg)') # Amount donated by the user (max is $9999999 for one donation)
     date = models.DateTimeField()
     def __str__(self):
        return str(self.userID.userID)

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
    
    
class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')

    def __str__(self):
        return f"${self.amount} - {self.status}"    
    


        

'''from django.db import models
from django.utils import timezone



    
   
   
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
    
   ''' 