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
    colorpic1 = CloudinaryField("media", blank=True, null=True)
    colorname1 = models.CharField(max_length=100)
    colorpic2 = CloudinaryField("media", blank=True, null=True)
    colorname2 = models.CharField(max_length=100)
    colorpic3 = CloudinaryField("media", blank=True, null=True)
    colorname3 = models.CharField(max_length=100)
    colorpic4 = CloudinaryField("media", blank=True, null=True)
    colorname4 = models.CharField(max_length=100)
    colorpic5 = CloudinaryField("media", blank=True, null=True)
    colorname5 = models.CharField(max_length=100)
    colorpic6 = CloudinaryField("media", blank=True, null=True)
    colorname6 = models.CharField(max_length=100)
    
class CarGallery(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    Exterior_1 = CloudinaryField("media", blank=True, null=True)
    Exterior_2 = CloudinaryField("media", blank=True, null=True)
    Exterior_3 = CloudinaryField("media", blank=True, null=True)
    Exterior_4 = CloudinaryField("media", blank=True, null=True)
    Exterior_5 = CloudinaryField("media", blank=True, null=True)
    Exterior_6 = CloudinaryField("media", blank=True, null=True)
    Exterior_7 = CloudinaryField("media", blank=True, null=True)
    Exterior_8 = CloudinaryField("media", blank=True, null=True)
    Interior_1 = CloudinaryField("media", blank=True, null=True)
    Interior_2 = CloudinaryField("media", blank=True, null=True)
    Interior_3 = CloudinaryField("media", blank=True, null=True)
    Interior_4 = CloudinaryField("media", blank=True, null=True)
    Interior_5 = CloudinaryField("media", blank=True, null=True)
    Interior_6 = CloudinaryField("media", blank=True, null=True)
    Interior_7 = CloudinaryField("media", blank=True, null=True)
    Interior_8 = CloudinaryField("media", blank=True, null=True)
    video_1 = models.FileField(upload_to='tests-videos/', blank=True, storage=VideoMediaCloudinaryStorage(),
                             validators=[validate_video])
    video_2 = models.FileField(upload_to='tests-videos/', blank=True, storage=VideoMediaCloudinaryStorage(),
                             validators=[validate_video])
    
class CarTech(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    Tech_pic1 = CloudinaryField("media", blank=True, null=True)
    Tech_name1 = models.CharField(max_length=100)
    Tech_desc_1 = models.TextField(blank=True)
    Tech_pic2 = CloudinaryField("media", blank=True, null=True)
    Tech_name2 = models.CharField(max_length=100)
    Tech_desc_2 = models.TextField(blank=True)
    Tech_pic3 = CloudinaryField("media", blank=True, null=True)
    Tech_name3 = models.CharField(max_length=100)
    Tech_desc_3 = models.TextField(blank=True)
    Tech_pic4 = CloudinaryField("media", blank=True, null=True)
    Tech_name4 = models.CharField(max_length=100)
    Tech_desc_4 = models.TextField(blank=True)
    Tech_pic5 = CloudinaryField("media", blank=True, null=True)
    Tech_name5 = models.CharField(max_length=100)
    Tech_desc_5 = models.TextField(blank=True)
    
class Carvarient(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    Varient_name_1 = models.CharField(max_length=100)
    Varient_desc_1 = models.TextField(blank=True)
    Var_price_1 = models.DecimalField(max_digits=10, decimal_places=2)
    Varient_name_2 = models.CharField(max_length=100)
    Varient_desc_2 = models.TextField(blank=True)
    Var_price_2 = models.DecimalField(max_digits=10, decimal_places=2)
    Varient_name_3 = models.CharField(max_length=100)
    Varient_desc_3 = models.TextField(blank=True)
    Var_price_3 = models.DecimalField(max_digits=10, decimal_places=2)
    Varient_name_4 = models.CharField(max_length=100)
    Varient_desc_4 = models.TextField(blank=True)
    Var_price_4 = models.DecimalField(max_digits=10, decimal_places=2)
    Varient_name_5 = models.CharField(max_length=100)
    Varient_desc_5 = models.TextField(blank=True)
    Var_price_5 = models.DecimalField(max_digits=10, decimal_places=2)
    
class carFuel(models.Model):
    FUEL_CHOICES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('hybrid', 'Hybrid'),
        ('electric', 'Electric'),
        ('cng', 'CNG'),
    ]

    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    Fuel_type_1 = models.CharField(max_length=100, choices=FUEL_CHOICES)
    Fuel_price_1 = models.DecimalField(max_digits=10, decimal_places=2)
    Fuel_type_2 = models.CharField(max_length=100, choices=FUEL_CHOICES, blank=True, null=True)
    Fuel_price_2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Fuel_type_3 = models.CharField(max_length=100, choices=FUEL_CHOICES, blank=True, null=True)
    Fuel_price_3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Fuel_type_4 = models.CharField(max_length=100, choices=FUEL_CHOICES, blank=True, null=True)
    Fuel_price_4 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Fuel_type_5 = models.CharField(max_length=100, choices=FUEL_CHOICES, blank=True, null=True)
    Fuel_price_5 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
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

    
