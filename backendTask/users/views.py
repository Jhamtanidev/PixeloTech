from django.shortcuts import render,redirect
from .models import *
from .sendotp import messagehandler
from django.contrib.auth import login
import random 
# Create your views here.
def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone_no = request.POST.get('mobile')
        
        check_user = User.objects.filter(email = email).first()
        check_profile = Profile.objects.filter(phone_no = phone_no).first()
        
        if check_user or check_profile:
            context = {'message' : 'User already exists' , 'class' : 'danger' }
            return render(request,'register.html' , context)
            
        user = User(email = email , first_name = name)
        user.save()
        otp = str(random.randint(1000 , 9999))
        profile = Profile(user = user , phone_no=phone_no , otp = otp) 
        profile.save()
        message_handler =messagehandler(phone_no,profile.otp).send_otp_on_phone()
        request.session['phone_no'] = phone_no
        return redirect('/otp')
    return render(request,'register.html')

def login_view(request):
    if request.method == 'POST':
        phone_no = request.POST.get('mobile')
        
        user = Profile.objects.filter(phone_no = phone_no).first()
        
        if user is None:
            context = {'message' : 'User not found' , 'class' : 'danger' }
            return render(request,'login.html' , context)
        
        otp = str(random.randint(1000 , 9999))
        user.otp = otp
        user.save()
        message_handler =messagehandler(phone_no,user.otp).send_otp_on_phone()
        request.session['phone_no'] = phone_no
        return redirect('/otp')        
    return render(request,'login.html')    


def otp_view(request):
    phone_no = request.session['phone_no']
    context = {'mobile':phone_no}
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Profile.objects.filter(phone_no=phone_no).first()
        
        if otp == profile.otp:
            login(request,profile.user)
            return redirect('/swipepic/dashboard/',context)
        else:
            print('Wrong')
            
            context = {'message' : 'Wrong OTP' , 'class' : 'danger','mobile':phone_no }
            return render(request,'otp.html' , context)
            
        
    return render(request,'otp.html' , context)

# for testing
# def dashboard_view(request):
#     return render(request,'dashboard.html')