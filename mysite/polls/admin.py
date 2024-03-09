from django.contrib import admin
from django.contrib import admin

# Register your models here.
from .models import Employee,Customer,Appointment,Event,Attendee
admin.site.register(Employee),
admin.site.register(Customer),
admin.site.register(Appointment)
admin.site.register(Event)
admin.site.register(Attendee)
   
from .models import *
from django.contrib import admin
from .models import (CarModel,CarColor,CarGalleryInte,CarGalleryVid,CarGalleryExt,CarTech,Carvarient,
    carFuel,carinfo,Generalinfo, Customer, Dealer, Employee, Appointment,Attendee,Event,)

# Define a custom admin site for cars-related models
admin.site.register(CarModel)
admin.site.register(CarColor)
admin.site.register(CarGalleryInte)
admin.site.register(CarGalleryVid)
admin.site.register(CarGalleryExt)
admin.site.register(CarTech)
admin.site.register(Carvarient)
admin.site.register(carFuel)
admin.site.register(carinfo)
admin.site.register(Generalinfo)
admin.site.register(CarBooking)
admin.site.register(Dealer)

