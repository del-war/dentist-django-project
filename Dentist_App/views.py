from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        #send an email
        send_mail(
            message_name, #subject
            message, #message
            message_email, #from email
            ['delwar.ewubd@gmail.com'], # To Email
        )

        dict = {
            'message_name':message_name
        }

        return render(request, 'contact.html', context=dict )

    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})

def service(request):
    return render(request, 'service.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def blog_details(request):
    return render(request, 'blog-details.html', {})

def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_scheldule = request.POST['your-scheldule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']

        #send an email
        appointment = "Name: " + your_name + " Phone: "+ your_phone + "Email: " + your_email + "Address : " + your_address + " Schedule : "+ your_scheldule + " Day: "+ your_date + "Message :" + your_message
        send_mail(
            'Appointment Request', #subject
            appointment, #message
            your_email, #from email
            ['delwar.ewubd@gmail.com'], # To Email
        )

        dict = {
            'your_name':your_name,
            'your_phone':your_phone,
            'your_email':your_email,
            'your_address':your_address,
            'your_scheldule':your_scheldule,
            'your_date':your_date,
            'your_message':your_message

        }

        return render(request, 'appointment.html', context=dict )

    else:
        return render(request, 'home.html', {})




