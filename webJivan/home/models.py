from django.db import models
from django.utils import timezone

# Create your models here.

class Client(models.Model):
    FullName = models.TextField(max_length=100)
    bloodGroup = models.EnumField(choices=['A+','A-','B+','B-','O+','O-','AB+','AB-'])
    Gender= models.EnumField(choices=['Male','Female','Others'])
    DateOfBirth = models.DateTimeField(default=timezone.now)
    MobileNumber = models.TextField(max_length=12)
    AlternateMobileNumber= models.TextField(max_length=12)
    Email=models.EmailField()
    Address=models.TextField(max_length=100)
    Pincode=models.TextField(max_length=20)
    State=models.TextField(max_length=20)
    Country=models.TextField(max_length=25)
    Professional_Status=models.EnumField(choices=['Private Service','Govt Service'])
    
