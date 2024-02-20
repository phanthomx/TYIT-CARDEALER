from django.contrib import admin
from django.contrib import admin

# Register your models here.
from .models import Employee,Customer,Appointment,Event,Attendee
admin.site.register(Employee),
admin.site.register(Customer),
admin.site.register(Appointment)
admin.site.register(Event)
admin.site.register(Attendee)
   

from django.contrib import admin
from .models import CarModel, CarColor, CarGallery, CarTech, Carvarient, carFuel, carinfo, Generalinfo

# Define a custom admin site for cars-related models
admin.site.register(CarModel)
admin.site.register(CarColor)
admin.site.register(CarGallery)
admin.site.register(CarTech)
admin.site.register(Carvarient)
admin.site.register(carFuel)
admin.site.register(carinfo)
admin.site.register(Generalinfo)


