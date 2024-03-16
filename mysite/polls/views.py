from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db import connection
import hashlib

# Import models once
from .models import (CarModel,CarColor,CarGalleryInte,CarGalleryVid,CarGalleryExt,CarTech,Carvarient,
    carFuel,carinfo,Generalinfo, Customer, Dealer, Employee, Appointment,Attendee,Event,)

import csv
from django.http import HttpResponse, FileResponse
import tempfile
import os

from datetime import datetime, timedelta, date
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import render
import razorpay
from razorpay.errors import BadRequestError
from django.views.decorators.csrf import csrf_exempt

from urllib.parse import urlencode



def polls(request):
    return render(request, 'polls/login.html')

def home(request):
    return render(request,'polls/Home.html')
  

def login(request):
    return render(request, 'polls/login.html')

def elogin(request):
    return render(request, 'polls/LoginEmp.html')
def EmpLogin(request):
    return render(request, 'polls/LoginEmp.html')
def buy(request):
        carmodel = CarModel.objects.all()
        # Pass the events to the template for rendering

        return render(request, 'polls/buy.html', {'car_models': carmodel})
   
def showcar(request):
    if request.method == "POST":
        carname = request.POST.get("car_name")
        model = CarModel.objects.get(name=carname)
        car_media_Int = CarGalleryInte.objects.filter(car_model=model)
        car_media_Ext = CarGalleryExt.objects.filter(car_model=model)
        car_media_Vid = CarGalleryVid.objects.filter(car_model=model)
        tech = CarTech.objects.filter(car_model=model)
        color = CarColor.objects.filter(car_model=model)
        varients = Carvarient.objects.filter(car_model=model)
        fuel = carFuel.objects.filter(car_model=model)
        info = carinfo.objects.filter(car_model=model).all()
        genfo = Generalinfo.objects.filter(car_model=model)
\
        
        return render(request, 'polls/car_dtail.html', {
    'Model_info': model,
    'CarMedia_Int': car_media_Int,
    'CarMedia_Ext': car_media_Ext,
    'CarMedia_Vid': car_media_Vid,
    'Tech': tech,
    'varients': varients,
    'fuel': fuel,
    'info': info,
    'genfo': genfo,
    'colors': color
})     
    return render(request, 'polls/buy.html')
def service(request):
    return render(request, 'polls/service.html')

def eservice(request):
    return render(request, 'polls/EmpServ.html')
def events(request):
    if request.method == 'POST':
        event = request.POST.get('event_name')  # Assuming the event name is passed from the form
        current_datetime = timezone.now()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        eventAttendess = request.POST.get('eventta')
        print(eventAttendess)
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM polls_Attendee WHERE event =%s", [event])
        count_result = cursor.fetchone()
        attendee_count = count_result[0]
        print(attendee_count)
        # Optionally, you can display a success message
        if int(attendee_count) < int(eventAttendess):
                    messages.success(request, 'Thank you for your registration!')
                    attendee = Attendee.objects.create(event=event, name=name, email=email, phone=phone)
                    attendee.save()
                    moe = "Your registration is scuccessful"

        else:
                    moe = "Sorry registrations are full" 
        # Retrieve events again to update the context with the latest data
        events = Event.objects.all()
        # Pass the success message and events to the template for rendering
        return render(request, 'polls/events.html', {'events': events, 'success_message': moe , 'eventname': event })

    else:
        events = Event.objects.all()
        # Pass the events to the template for rendering
        return render(request, 'polls/events.html', {'events': events})
def chome(request):
        return render(request, 'polls/eafter.html')

@login_required
def ehome(request):
    return render(request, 'polls/empafter.html')

def loginverify(request):
    print("-----------login verification------------")
    if request.method == "POST":
        cemail = request.POST.get("cemail")
        cpassword = request.POST.get('cpassword')
        print(cemail, cpassword)
        all_customers = Customer.objects.all()

        # Print the users (for debugging purposes)
        elist, epass = [], []
        for customer in all_customers:
            elist.append(customer.Email)
            epass.append(customer.password)
            print(customer.Email, customer.password)
        try:
            n = elist.index(cemail)
            m = epass.index(str(cpassword))
            print(elist, epass)
            if n == m:
                user = authenticate(request, Email=cemail, password=cpassword)
                auth_login(request,user)

                print("no problem")
                messages.success(request, 'Login customer successful')
                redirect_url = '/chome/'
                return JsonResponse({'redirect_url': redirect_url})   
            else:
                raise ValueError("Invalid email or password")
        except ValueError as e:
            messages.error(request, str(e))
            print("problem occurred")
            redirect_url = '/Registration/'
            return JsonResponse({'redirect_url': redirect_url})
    # If request method is not POST or if there's an issue with the request
    return JsonResponse({'redirect_url': '/Registration/'})
def emploginverify(request):
    print("----------- Emplogin verification------------")
    if request.method == "POST":
        eemail = request.POST.get("eemail")
        epassword = request.POST.get('epassword')
        print(eemail, epassword)
        all_employees = Employee.objects.all()  # Corrected variable name
        elist, epass = [], []
        for employee in all_employees:  # Corrected variable name
            elist.append(employee.Empemail)
            epass.append(employee.Emppassword)
            print(employee.Empemail, employee.Emppassword)
        try:
            n = elist.index(eemail)
            m = epass.index(str(epassword))
            print(elist, epass)
            if n == m:   
                user = authenticate(request, Empemail=eemail, Emppassword=epassword)
                print(user)
                if user is not None:
                    print(user)
                    login(request, user)
                print(user)
                auth_login(request,user)
                print("no problem")
                messages.success(request, 'Login  emp successful')
                messagess = True
                redirect_url = '/ehome/'
                return JsonResponse({'redirect_url': redirect_url})
            else:
                messages.error(request, 'Invalid email or password')
                print("problem occurred")
                redirect_url = '/EmpR/'
                return JsonResponse({'redirect_url': redirect_url})  
        except ValueError:
            messages.error(request, 'Invalid email or password')
            print("problem occurred")
            redirect_url = '/EmpR/'
            return JsonResponse({'redirect_url': redirect_url})  
    template = 'polls/CustLandingpage.html'
    return render(request, template)

def Registration(request):
    return render(request, 'polls/Crregis.html')

def EmpRegistration(request):
    return render(request, 'polls/EmpRegia.html')
def defaultpg(request):
    if request.method == "POST":
        # Use request.POST.get() to retrieve form data
        name = request.POST.get("name")
        email = request.POST.get('email')
        password = request.POST.get('password')
        new_cus = Customer(name=name,Email=email,password=password)
        new_cus.save()
        template = 'polls/EmpLogin.html'
        return render(request, template)
    # You may want to handle the case when the request method is not POST
    template = 'polls/EmpLogin.html'
    return render(request, template)

def emphome(request):
    if request.method == "POST":
        # Use request.POST.get() to retrieve form data
        name = request.POST.get("name")
        email = request.POST.get('email')
        password = request.POST.get('password')
        new_emp = Employee(Empname=name,Empemail=email,Emppassword=password)
        new_emp.save()
        template = 'polls/EmpLogin.html'
        return render(request, template)
    # You may want to handle the case when the request method is not POST
    template = 'polls/EmpLogin.html'
    return render(request, template)
def hi(request):
        return render(request, 'polls/EmpReg.html')
def servicereq(request):
    print("----------Service req recieved---------")
    if request.method == "POST":
        name = request.POST.get("cliname")
        email = request.POST.get("cliemail")
        phone = request.POST.get("cliphone")
        modelName = request.POST.get("modelName")
        registrationNumber = request.POST.get("registrationNumber")
        appointmentDate = request.POST.get("appointmentDate")
        appointmentTime = request.POST.get("appointmentTime")
        all_appointment = Appointment.objects.all()
        print("+++++++++++++++++++")
        print(email)
        for apps in all_appointment:
            print(apps)
            
        start_date = date.today()
        end_date = appointmentDate  # Adjust as needed
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM polls_appointment WHERE appointment_date = %s AND appointment_time = %s", [appointmentDate, appointmentTime])
        count_result = cursor.fetchone()[0]
        appointment_count = count_result
        print(appointment_count)
        token_data = f"{email}{appointmentDate}{appointmentTime}"
        hashed_token = hashlib.sha256(token_data.encode()).hexdigest()
        token = hashed_token[:10]
        if appointment_count == 0 :
            newserv=Appointment(name=name,email=email,phone=phone,model_name=modelName,registration_number=registrationNumber,appointment_date=appointmentDate,appointment_time=appointmentTime,count="1",token=token)
            newserv.save()
            print("slot available")
            subject = "Regarding your Service Appointment"
            message = f"Thanks {name} for booking your service appointment with us at {appointmentTime} on date {appointmentDate}  your token is {token}"
            send_mail(subject, message, "athenamcgonagall7@gmail.com", [email])
            
        if appointment_count  < 6  and appointment_count >= 1:
            newserv=Appointment(name=name,email=email,phone=phone,model_name=modelName,registration_number=registrationNumber,appointment_date=appointmentDate,appointment_time=appointmentTime,count=appointment_count+1,token=token)
            newserv.save()
            print("slot available")
            subject = "Regarding your Service Appointment"
            message = f"Thanks {name} for booking your service appointment with us at {appointmentTime} on date {appointmentDate} your token is {token}"
            send_mail(subject, message, "athenamcgonagall7@gmail.com", [email])
        else:
            print("Slot not available")
 # Assng Employee is your model for employees
        print(name, email, phone, modelName, registrationNumber, appointmentDate, appointmentTime)
        redirect_url = '/chome/'
        return JsonResponse({'redirect_url': redirect_url})


def getservice(request):
    if request.method == "POST":
        appointmentDate = request.POST.get("appointmentDate")
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT name, email, phone, appointment_time, token FROM polls_appointment WHERE appointment_date = %s ORDER BY appointment_time ASC", [appointmentDate])
        query_result = cursor.fetchall()
        
        if not query_result:
            return render(request, 'polls/EmpServ.html', {'appointmentDate': appointmentDate})

        # Create CSV data
        csv_data = [
            ['Name', 'Email', 'Phone', 'Appointment Time', 'Token']
        ]
        for row in query_result:
            csv_data.append(row)

        # Convert CSV data to string
        csv_content = '\n'.join([','.join(map(str, row)) for row in csv_data])

        # Offer CSV content for download via render
        context = {
            'query_result': query_result,
            'csv_content': csv_content
        }

        return render(request, 'polls/EmpServ.html', context)

    return render(request, 'polls/EmpServ.html')


from django.shortcuts import render
from polls.models import Attendee  # Assuming the model name is Attendee

from polls.models import Event  # Import the Event model

from polls.models import Event  # Import the Event model

def getevent(request):
    if request.method == "POST":
        eventname = request.POST.get("selected_event")
        print(eventname)
        attendees = Attendee.objects.filter(event=eventname)
        event_list = Event.objects.values_list('event_name', 'date_time').distinct()
        csv_data = [
            ['Name', 'Email', 'Phone', 'Event', 'Registration Date']
        ]
        for attendee in attendees:
            csv_data.append([attendee.name, attendee.email, attendee.phone, attendee.event, attendee.registration_date])
        csv_content = '\n'.join([','.join(map(str, row)) for row in csv_data])

        return render(request, 'polls/EmpEvents.html', {'events': event_list, 'attendees': attendees,'csv_content': csv_content})
    else:
        event_list = Event.objects.values_list('event_name', 'date_time').distinct()

        return render(request, 'polls/EmpEvents.html', {'events': event_list})


import json

def orderinfo(request):
    
    if request.method == 'POST':
        # Access the data sent from the form
        variant_type = request.POST.get('selected_varient')
        fuel_type = request.POST.get('selected_fuel')
        color = request.POST.get('selected_color')
        booking_price = request.POST.get('bookingAmount')
        model_name = request.POST.get('modelName')
        total_price = request.POST.get('tot_price')
        print(variant_type, fuel_type, color, booking_price, model_name, total_price)
        client = razorpay.Client(auth=("rzp_test_eAkHPAnkDkrRNg", "we8dV3Z1IqeYhDSoFbdubLZ7"))
        payment = client.order.create({'amount': booking_price, 'currency': 'INR', 'payment_capture': '1'})
        razorpay_order_id = payment['id']
        print(payment)   
        callback_url = '/initiate_payment/'    
        context = {
        'variant_type': variant_type,
        'fuel_type': fuel_type,
        'color': color,
        'booking_price': booking_price,
        'razorpay_order_id':razorpay_order_id,
        'payment':payment,
        'callback_url':callback_url,
        'model_name': model_name,
        'total_price': total_price,

    }
    
        return render(request, 'polls/order.html', context)

    else:
        return HttpResponse("This view only accepts POST requests.")
def show_payment(request):
     return render(request, 'polls/order.html')
 
# @csrf_exempt
from django.shortcuts import render
from .models import CarBooking  # Import the CarBooking model

def initiate_payment(request):
    print("----------")
    if request.method == "POST":
        var_type = request.POST.get('variant_type')
        fuel = request.POST.get('fuel_type')
        color_n = request.POST.get('color')
        amount = request.POST.get('booking_price')
        model = request.POST.get('model_name')
        print(amount)
        tot_price = request.POST.get('total_price')
        fname = request.POST.get('fname')
        print(fname)
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        payid = request.POST.get('razorpay_order_id')
        print(payid)
        file1 = request.POST.get('file1')
        file2 = request.POST.get('file2')
        print(file1,file2)
        new_entry = CarBooking(
            var_type=var_type,
            fuel=fuel,
            color_n=color_n,
            amount=amount,
            model=model,
            tot_price=tot_price,
            fname=fname,
            lname=lname,
            phone=phone,
            email=email,
            address=address,
            file1=file1,
            file2=file2,
            orderid=payid
        )
        Deal = Dealer(payment_id=payid,dealer_no="Asc0001",amount=amount,customer_email=email,car_model=model)
        # Save the instance to the database
        new_entry.save()
        Deal.save()
        return render(request, 'polls/payment_success.html')
    else:
        return render(request, 'polls/payment_failure.html')

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def payment_success(request):
    return render(request, 'polls/payment_success.html')

def payment_failure(request):
    return render(request, 'polls/payment_failure.html')
 
def empbuy(request):
    date = request.GET.get('date') 
    print("-----------")# Retrieve date from query parameters
    print(date)
    if date:
        bookings = CarBooking.objects.filter(created_at=date)
        csv_data = [
        ['Model', 'Variant Type', 'Fuel', 'Color', 'Amount', 'Total Price',
         'First Name', 'Last Name', 'Phone', 'Email', 'Address', 'Order ID', 'Created At']
            ]
        for booking in bookings:
            csv_data.append([
            booking.model, booking.var_type, booking.fuel, booking.color_n,
            booking.amount, booking.tot_price, booking.fname, booking.lname,
            booking.phone, booking.email, booking.address, booking.orderid, booking.created_at
        ])
    # Convert CSV data to string
        csv_content = '\n'.join([','.join(map(str, row)) for row in csv_data])
    else:
        # If no date is provided, retrieve all bookings
        bookings = CarBooking.objects.all()
        csv_data = [
        ['Model', 'Variant Type', 'Fuel', 'Color', 'Amount', 'Total Price',
         'First Name', 'Last Name', 'Phone', 'Email', 'Address', 'Order ID', 'Created At']
            ]
        for booking in bookings:
            csv_data.append([
            booking.model, booking.var_type, booking.fuel, booking.color_n,
            booking.amount, booking.tot_price, booking.fname, booking.lname,
            booking.phone, booking.email, booking.address, booking.orderid, booking.created_at
        ])
    # Convert CSV data to string
        csv_content = '\n'.join([','.join(map(str, row)) for row in csv_data])
    # Pass bookings and date to the template context
    return render(request, 'polls/empbuy.html', {'bookings': bookings, 'date': date,'csv_content': csv_content})