from random import randrange
from myapp.models import User
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
        try:
                uid = User.objects.get(email=request.session['email'])
                return render(request,'index.html',{'uid':uid})
        except:
                return render(request,'pages_login.html')
    
def pages_register(request):
        if request.method == "POST": 
                try:
                        User.objects.get(email=request.POST['email'])
                        msg = "email is already registered"
                        return render(request, 'pages_register.html',{'msg':msg})
                except:
                        if request.POST['password'] == request.POST['repassword']:
                                otp = randrange(1000,9999)
                                subject = 'OTP Verification'
                                message = f'Your OTP is {otp}'
                                email_from = settings.EMAIL_HOST_USER
                                recipient_list = [request.POST['email'], ]
                                send_mail( subject,message, email_from, recipient_list)
                                global temp
                                temp = {
                                        'name' : request.POST['name'],
                                        'dob'  : request.POST['dob'],
                                        'email' : request.POST['email'],
                                        'mobile' : request.POST['mobile'],  
                                        'address' : request.POST['address'],  
                                        'password' : request.POST['password'],
                                        'repassword' : request.POST['repassword'],
                                        'mobile' : request.POST['mobile'],

                                        }

                                return render (request,'otp.html',{'msg':'OTP send on your email!!','otp':otp})
                        return render (request,'otp.html',{'msg':'OTP send on your email!!','otp':otp})
                
        return render(request,'pages_register.html')

def otp(request):
        try:

                if request.POST['uotp'] == request.POST['otp']:
                        global temp
                        User.objects.create (
                                name = temp['name'],
                                dob  = temp['dob'],
                                email = temp['email'],
                                mobile = temp['mobile'],  
                                address = temp['address'],  
                                password = temp['password'],                       
                        )
                        del temp
                        return render(request,'pages_login.html',{'msg':'Account Created'})
                return render(request,'otp.html',{'msg' :'Invalid OTP','otp':request.POST['otp']})
        except:
                return redirect('pages_register')
        
def pages_login(request):
        if request.method == 'POST':
                 try:
                         uid = User.objects.get(email=request.POST
                         ['email'])
                         if request.POST['password'] == uid.password:
                                 request.session['email'] = request.POST['email']
                                 return redirect('index')               
                         return render(request, 'index.html',{'uid':uid})
                        
                 except:
                        
                         return render(request,'pages_login.html',{'msg':'Acccount does not exists'})
        return render(request , 'pages_login.html')
             
                
        
def users_profile(request):
        return render(request,'users_profile.html')

def logout(request):
        try: 
                request.session['email']
                del request.session['email']
                return render(request, 'pages_login.html')
        except:
        
                return render(request,'pages_login.html')