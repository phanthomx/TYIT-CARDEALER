from django.contrib import admin
from django.contrib import admin

# Register your models here.
from .models import Employee,Customer,Appointment,Event
admin.site.register(Employee),
admin.site.register(Customer),
admin.site.register(Appointment)
admin.site.register(Event)
   


