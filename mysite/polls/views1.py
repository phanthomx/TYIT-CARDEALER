# from django.shortcuts import render, redirect
# from django.http import HttpResponse, JsonResponse
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# from django.contrib.auth import login as auth_login
# from django.contrib import messages
# from django.core.mail import send_mail
# from django.conf import settings
# from django.db import connection
# from django.contrib.auth import login, authenticate

# from datetime import datetime, timedelta, date
# from .models import Customer, Employee, Appointment, Attendee, Event
# import hashlib
# from django.utils import timezone
# from django.contrib.auth.decorators import login_required

# def your_view(request):
#     # Your view code here
#     pass

# def polls(request):
#     return render(request, 'polls/login.html')

# def home(request):
#     return render(request,'polls/Home.html')
  

# def login(request):
#     return render(request, 'polls/login.html')

# def elogin(request):
#     return render(request, 'polls/LoginEmp.html')
# def EmpLogin(request):
#     return render(request, 'polls/LoginEmp.html')
# def buy(request):
#     return render(request, 'polls/buy.html')
# def service(request):
#     return render(request, 'polls/service.html')

# def eservice(request):
#     return render(request, 'polls/EmpServ.html')
# def events(request):
#     if request.method == 'POST':
#         event = request.POST.get('event_name')  # Assuming the event name is passed from the form
#         current_datetime = timezone.now()
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         eventAttendess = request.POST.get('eventta')
#         print(eventAttendess)
#         cursor = connection.cursor()
#         cursor.execute("SELECT COUNT(*) FROM polls_Attendee WHERE event =%s", [event])
#         count_result = cursor.fetchone()
#         attendee_count = count_result[0]
#         print(attendee_count)
#         # Optionally, you can display a success message
#         if int(attendee_count) < int(eventAttendess):
#                     messages.success(request, 'Thank you for your registration!')
#                     attendee = Attendee.objects.create(event=event, name=name, email=email, phone=phone)
#                     attendee.save()
#                     moe = "Your registration is scuccessful"

#         else:
#                     moe = "Sorry registrations are full"

            
#         # Retrieve events again to update the context with the latest data
#         events = Event.objects.all()
#         # Pass the success message and events to the template for rendering
#         return render(request, 'polls/events.html', {'events': events, 'success_message': moe , 'eventname': event })

#     else:
#         events = Event.objects.all()
#         # Pass the events to the template for rendering
#         return render(request, 'polls/events.html', {'events': events})
# def chome(request):

#         return render(request, 'polls/eafter.html')

# @login_required
# def ehome(request):
#     return render(request, 'polls/empafter.html')

# def loginverify(request):
#     print("-----------login verification------------")
#     if request.method == "POST":
#         cemail = request.POST.get("cemail")
#         cpassword = request.POST.get('cpassword')
#         print(cemail, cpassword)
#         all_customers = Customer.objects.all()

#         # Print the users (for debugging purposes)
#         elist, epass = [], []
#         for customer in all_customers:
#             elist.append(customer.Email)
#             epass.append(customer.password)
#             print(customer.Email, customer.password)
        
#         try:
#             n = elist.index(cemail)
#             m = epass.index(str(cpassword))
#             print(elist, epass)
#             if n == m:
#                 user = authenticate(request, Email=cemail, password=cpassword)
#                 login(user)

#                 print("no problem")
#                 messages.success(request, 'Login customer successful')
#                 redirect_url = '/chome/'
#                 return JsonResponse({'redirect_url': redirect_url})
                
#             else:
#                 raise ValueError("Invalid email or password")
#         except ValueError as e:
#             messages.error(request, str(e))
#             print("problem occurred")
#             redirect_url = '/Registration/'
#             return JsonResponse({'redirect_url': redirect_url})

#     # If request method is not POST or if there's an issue with the request
#     return JsonResponse({'redirect_url': '/Registration/'})

# def emploginverify(request):

#     print("----------- Emplogin verification------------")
#     if request.method == "POST":
#         eemail = request.POST.get("eemail")
#         epassword = request.POST.get('epassword')
#         print(eemail, epassword)
#         all_employees = Employee.objects.all()  # Corrected variable name
#         elist, epass = [], []
#         for employee in all_employees:  # Corrected variable name
#             elist.append(employee.Empemail)
#             epass.append(employee.Emppassword)
#             print(employee.Empemail, employee.Emppassword)
#         try:
#             n = elist.index(eemail)
#             m = epass.index(str(epassword))
#             print(elist, epass)
#             if n == m:
                
#                 user = authenticate(request, Empemail=eemail, Emppassword=epassword)
#                 print(user)
               
#                 if user is not None:
#                     print(user)
#                     login(request, user)
#                 print(user)
#                 login(request,user)
                
#                 print("no problem")
#                 messages.success(request, 'Login  emp successful')
#                 messagess = True
#                 redirect_url = '/ehome/'
#                 return JsonResponse({'redirect_url': redirect_url})
#             else:
#                 messages.error(request, 'Invalid email or password')
#                 print("problem occurred")
#                 redirect_url = '/EmpR/'
#                 return JsonResponse({'redirect_url': redirect_url})  
#         except ValueError:
#             messages.error(request, 'Invalid email or password')
#             print("problem occurred")
#             redirect_url = '/EmpR/'
#             return JsonResponse({'redirect_url': redirect_url})  

#     template = 'polls/CustLandingpage.html'
#     return render(request, template)

# def Registration(request):
#     return render(request, 'polls/Crregis.html')

# def EmpRegistration(request):
#     return render(request, 'polls/EmpRegia.html')
# def defaultpg(request):
#     print("-----------challa  bagh------------")
#     if request.method == "POST":
#         # Use request.POST.get() to retrieve form data
#         name = request.POST.get("name")
#         email = request.POST.get('email')
#         password = request.POST.get('password')

        
#         new_cus = Customer(name=name,Email=email,password=password)
#         new_cus.save()
        
#         template = loader.get_template('polls/EmpLogin.html')
#         return HttpResponse(template.render())
        

   

#     # You may want to handle the case when the request method is not POST
#     template = loader.get_template('polls/EmpLogin.html')
#     return HttpResponse(template.render())

# def emphome(request):
#     print("-----------Page worked------------")
#     if request.method == "POST":
#         # Use request.POST.get() to retrieve form data
#         name = request.POST.get("name")
#         email = request.POST.get('email')
#         password = request.POST.get('password')

        
#         new_emp = Employee(Empname=name,Empemail=email,Emppassword=password)
#         new_emp.save()
#         template = loader.get_template('polls/EmpLogin.html')
#         return HttpResponse(template.render())
        

   

#     # You may want to handle the case when the request method is not POST
#     template = loader.get_template('polls/EmpLogin.html')
#     return HttpResponse(template.render())
# def hi(request):
#         return render(request, 'polls/EmpReg.html')
# def servicereq(request):
#     print("----------Service req recieved---------")
#     if request.method == "POST":
#         name = request.POST.get("cliname")
#         email = request.POST.get("cliemail")
#         phone = request.POST.get("cliphone")
#         modelName = request.POST.get("modelName")
#         registrationNumber = request.POST.get("registrationNumber")
#         appointmentDate = request.POST.get("appointmentDate")
#         appointmentTime = request.POST.get("appointmentTime")
#         all_appointment = Appointment.objects.all()
#         print("+++++++++++++++++++")
#         print(email)
#         for apps in all_appointment:
#             print(apps)
            
#         start_date = date.today()
#         end_date = appointmentDate  # Adjust as needed
#         cursor = connection.cursor()
#         cursor.execute("SELECT COUNT(*) FROM polls_appointment WHERE appointment_date = %s AND appointment_time = %s", [appointmentDate, appointmentTime])
#         count_result = cursor.fetchone()[0]
#         appointment_count = count_result
#         print(appointment_count)
#         token_data = f"{email}{appointmentDate}{appointmentTime}"
#         hashed_token = hashlib.sha256(token_data.encode()).hexdigest()
#         token = hashed_token[:10]
#         if appointment_count == 0 :
#             newserv=Appointment(name=name,email=email,phone=phone,model_name=modelName,registration_number=registrationNumber,appointment_date=appointmentDate,appointment_time=appointmentTime,count="1",token=token)
#             newserv.save()
#             print("slot available")
#             subject = "Regarding your Service Appointment"
#             message = f"Thanks {name} for booking your service appointment with us at {appointmentTime} on date {appointmentDate}  your token is {token}"
#             send_mail(subject, message, "athenamcgonagall7@gmail.com", [email])
            
#         if appointment_count  < 6  and appointment_count >= 1:
#             newserv=Appointment(name=name,email=email,phone=phone,model_name=modelName,registration_number=registrationNumber,appointment_date=appointmentDate,appointment_time=appointmentTime,count=appointment_count+1,token=token)
#             newserv.save()
#             print("slot available")
#             subject = "Regarding your Service Appointment"
#             message = f"Thanks {name} for booking your service appointment with us at {appointmentTime} on date {appointmentDate} your token is {token}"
#             send_mail(subject, message, "athenamcgonagall7@gmail.com", [email])
#         else:
#             print("Slot not available")
#  # Assng Employee is your model for employees
#         print(name, email, phone, modelName, registrationNumber, appointmentDate, appointmentTime)
#         redirect_url = '/chome/'
#         return JsonResponse({'redirect_url': redirect_url})
   

# def getservice(request):
#     if request.method == "POST":
#                 appointmentDate = request.POST.get("appointmentDate")
#                 print(appointmentDate)
#                 cursor = connection.cursor()
#                 cursor.execute("SELECT DISTINCT name,email,phone,appointment_time , token FROM polls_appointment WHERE appointment_date = %s ORDER BY appointment_time ASC", [appointmentDate])
#                 count_result = cursor.fetchall()
#                 context = {'query_result': count_result}
#                 return render(request, 'polls/EmpServ.html', context)
               
#     return render(request, 'polls/EmpServ.html', context)
        