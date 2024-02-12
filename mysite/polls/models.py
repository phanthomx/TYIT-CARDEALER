from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(models.Model):
  name = models.CharField(max_length=20)
  Email = models.CharField(max_length=50)
  password = models.CharField(max_length=20)
    

        
  USERNAME_FIELD = 'Email'
  REQUIRED_FIELDS = ['name']




class Employee(models.Model):
  Empname = models.CharField(max_length=20)
  Empemail = models.CharField(max_length=50)
  Emppassword = models.CharField(max_length=20)
  
  USERNAME_FIELD = 'Empemail'
  REQUIRED_FIELDS = ['Empname']
  

class Appointment(models.Model):
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)  # Adjust max_length as needed
    model_name = models.CharField(max_length=15)
    registration_number = models.CharField(max_length=20)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    count=models.IntegerField()

    def __str__(self):
        return self.name