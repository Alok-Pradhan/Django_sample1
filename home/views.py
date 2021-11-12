from django.shortcuts import redirect, render, HttpResponse
from home.models import Login
from datetime import datetime
from home.models import Signup
from django.contrib import messages
from django.contrib.auth import authenticate, login
import sys
import pprint
from time import sleep
#import pandas as pd
from django.shortcuts import render
from home.models import EmailForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from twilio.rest import Client
#from instapy import InstaPy
#from instapy import smart_run
#from InstagramAPI import InstagramAPI

#from phonenumbers import geocoder
# Create your views here.
def index(request):

    # context = {
    #     "name" : "alok"
    # }
    name = "alok"
    messages.success(request, 'Contact request submitted successfully.')
    return render(request , 'index.html', {"name" : name})

#ALok@123$
# return HttpResponse("this is home page")
def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        desc = request.POST.get('desc')
        login = Login(name = name, email = email,password = password, desc = desc,date = datetime.today())
        login.save()
    return render(request, 'login.html')

def signupa(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        #contact = request.POST.get('contact')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        signup = Signup(fname = fname , lname = lname, uname = uname , email = email, password = password)
        signup.save()
        # con = phonenumbers.parse(contact,"CH")
        #print(con)
        print("signup successfully")
        messages.success(request, 'Contact request submitted successfully.')

    return render (request, 'signup.html')

def auth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username = username, password = password)
        if user is not None:
           
            # login(request, user)
            # return redirect('/login')
            return redirect('/')
            #print("authenticate")
        else:
            # return render(request, 'auth.html')
            print("Unaurthorised")
    return render(request, 'auth.html')

           
# def sendSimpleEmail(emailto):
#    res = send_mail("hello paul", "comment tu vas?", "alokp2234@gmal.com", [emailto])
#    print("hello world")
#    return HttpResponse('%s'%res)

def mail(request):
    for i in range(1000):
        send_mail('Congratulation',
        'hello this is jerry here i wishing you a very happy diwali !',
        settings.EMAIL_HOST_USER,
        ['ranjitagouda39@gmail.com']
    )
    return render(request, "email.html")

def sms_send(request):
    message_to_broadcast = ("Hello this is Alok ! Have a good day "
                                                "you can learn python from www.w3school.com")
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,
                                   from_=settings.TWILIO_NUMBER,
                                   body=message_to_broadcast)
    return HttpResponse("messages sent!", 200)

# my_username = 'alok_pradhan02'
# my_password = 'Alok@2234'
# session = InstaPy(username=my_username, password=my_password,headless_browser=False)

# with smart_run(session):
#     session.set_relationship_bounds(
#         enable = True,
#         delimit_by_numbers=True,
#         max_followers=500,
#         min_followers=400,
#         min_following=30
#     )
#     session.set_do_follow(True , percentage = 100)
#     session.set_dont_like(['nsfw'])
#     session.like_by_tags(['bmw','mercedes', 'audi'], amount = 10)


   