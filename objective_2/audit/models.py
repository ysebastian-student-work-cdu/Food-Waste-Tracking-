from django.db import models
from django.core.validators import MinLengthValidator


class UserRoles(models.Model):
    roleID = models.IntegerField(primary_key=True)
    roleName = models.CharField(max_length=32)

    # Override the default pluralisation of table names in the admin console
    class Meta:
        verbose_name_plural = "UserRoles"  # Specify the plural name

    def __str__(self):
        return self.roleName

class Users(models.Model):
    userID = models.AutoField(primary_key=True)
    roleID = models.ForeignKey(
        UserRoles,
        on_delete=models.CASCADE,
        db_column='roleID'
    )
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

    # Override the default pluralisation of table names in the admin console
    class Meta:
        verbose_name_plural = "Users"  # Specify the plural name

    def __str__(self):
        return self.username


class organisation(models.Model):
    id = models.AutoField(primary_key=True)    
    f_name= models.CharField('Organisation Name', max_length=90)
    l_name= models.CharField('Organisation Name', max_length=90)
    description= models.TextField(blank=True)
    type= models.CharField('Organisation Type', max_length=90)
    
    
    def __str__(self):
        return self.name

class Donate(models.Model):
     userID= models.ForeignKey(Users, on_delete = models.CASCADE) # foreign key of userID in user table
     orgID= models.CharField('Organisation Name', max_length=90) # Foreigh  key of organisation id field
     amount = models.DecimalField(max_digits=7, decimal_places=2) # Amount donated by the user (max is $9999999 for one donation)
     
     def __str__(self):
        return self.name




        

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