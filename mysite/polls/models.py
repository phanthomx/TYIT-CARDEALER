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
  
