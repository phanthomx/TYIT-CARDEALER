
from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import MediaCloudinaryStorage, RawMediaCloudinaryStorage, VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Customer(models.Model):
  name = models.CharField(max_length=20)
  Email = models.CharField(max_length=50, primary_key=True, unique=True)
  password = models.CharField(max_length=20)
    

        
  USERNAME_FIELD = 'Email'
  REQUIRED_FIELDS = ['name']




class Employee(models.Model):
  Empname = models.CharField(max_length=20)
  Empemail = models.CharField(max_length=50, primary_key=True, unique=True)
  Emppassword = models.CharField(max_length=20)
  
  USERNAME_FIELD = 'Empemail'
  REQUIRED_FIELDS = ['Empname']
  

class Appointment(models.Model):
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)  # Adjust max_length as needed
    model_name = models.CharField(max_length=15)
    registration_number = models.CharField(max_length=20)
    token=models.CharField(max_length=100)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    count=models.IntegerField()

    

    def __str__(self):
        return self.name

class Event(models.Model):
    event_id = models.CharField(max_length=100, unique=True)
    event_name = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    event_description = models.CharField(max_length=500)
    event_total_attendees = models.IntegerField(blank=True, null=True)
    # Assuming you want to store URLs of photos or videos
    media_1 = CloudinaryField("media", blank=True, null=True)
    media_2 = CloudinaryField("media", blank=True, null=True)
    media_3 = CloudinaryField("media", blank=True, null=True)
    media_4 = CloudinaryField("media", blank=True, null=True)
    media_5 = CloudinaryField("media", blank=True, null=True)
    media_6 = CloudinaryField("media", blank=True, null=True)
    media_7 = CloudinaryField("media", blank=True, null=True)
    media_8 = CloudinaryField("media", blank=True, null=True)
    video_1 = CloudinaryField("video", blank=True, null=True)
    video = models.FileField(upload_to='tests-videos/', blank=True, storage=VideoMediaCloudinaryStorage(),
                             validators=[validate_video])

    def __str__(self):
        return self.event_name
  
@receiver(post_save, sender=Event)
def delete_past_events(sender, instance, **kwargs):
    if instance.date_time < timezone.now():
        instance.delete()
        
        
class Attendee(models.Model):
    # Define fields to store attendee information
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    event = models.CharField(max_length=200)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
      
class CarModel(models.Model):
    name = models.CharField(max_length=100,primary_key=True, unique=True)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.DecimalField(max_digits=10, decimal_places=2)
    coverpic = CloudinaryField("media", blank=True, null=True)

    

class CarColor(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    colorpic = CloudinaryField("media", blank=True, null=True)
    colorname = models.CharField(max_length=100)

class CarGalleryExt(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    Exterior = CloudinaryField("media", blank=True, null=True)
    
    
class CarGalleryInte(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    Interior = CloudinaryField("media", blank=True, null=True)
 
 
class CarGalleryVid(models.Model):
        car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
        video_1 = models.FileField(upload_to='tests-videos/', blank=True, storage=VideoMediaCloudinaryStorage(),
                             validators=[validate_video])
     
class CarTech(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    Tech_pic = CloudinaryField("media", blank=True, null=True)
    Tech_name = models.CharField(max_length=100)
    Tech_desc = models.TextField(blank=True)

class Carvarient(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    Varient_name = models.CharField(max_length=100)
    Varient_desc = models.TextField(blank=True)
    Var_price = models.DecimalField(max_digits=10, decimal_places=2)

class carFuel(models.Model):
    FUEL_CHOICES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('hybrid', 'Hybrid'),
        ('electric', 'Electric'),
        ('cng', 'CNG'),
    ]

    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    Fuel_type = models.CharField(max_length=100, choices=FUEL_CHOICES)
    Fuel_price = models.DecimalField(max_digits=10, decimal_places=2)

class carinfo(models.Model):
    OWNING_CHOICES = [
        ('first_hand', 'First Hand'),
        ('second_hand', 'Second Hand'),
        ('limited_edition', 'Limited Edition'),
    ]

    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    car_desc = models.TextField(blank=True)
    car_type = models.CharField(max_length=100)
    owning = models.CharField(max_length=100, choices=OWNING_CHOICES)
    units = models.IntegerField(blank=True, null=True)
  
class Generalinfo(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    max_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    booking_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    Delivery_time= models.CharField(max_length=100)
    emi  = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

class CarBooking(models.Model):
    var_type = models.CharField(max_length=100)
    fuel = models.CharField(max_length=100)
    color_n = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    model = models.CharField(max_length=100)
    tot_price = models.DecimalField(max_digits=10, decimal_places=2)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    file1 = CloudinaryField("media", blank=True, null=True)
    file2 = CloudinaryField("media", blank=True, null=True)
    paid = models.BooleanField(default=False)
    orderid = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)  # Automatically set the date and time when object is created

    def __str__(self):
        return f"{self.model} - {self.var_type}"