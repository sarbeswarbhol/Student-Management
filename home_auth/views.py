from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.crypto import get_random_string

# Import your User and PasswordResetRequest models
from .models import User, PasswordResetRequest

# Create your views here.
def signup_view(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']
        
        
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            role=role,
            )
        if role == 'student':
            user.is_student = True
        elif role == 'teacher':
            user.is_teacher = True
        elif role == 'admin':
            user.is_admin = True
            
        user.save()
        login(request, user)
        
        messages.success(request, "SignUp Successfully!")
        return redirect('index')
    return render(request,'authentication/register.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successful !')
            
            if user.is_admin:
                return redirect ('admin_dashboard')
            elif user.is_teacher:
                return redirect ('teacher_dashboard')
            elif user.is_student:
                return redirect ('dashboard')
            else :
                messages.error(request, "Invalid User role")
                return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')
    return render (request, "authentication/login.html")

def forgot_password_view(request):
    if request.method == "POST":
        email = request.POST['email']
        user = User.objects.filter(email=email).first()
        
        if user:
            token = get_random_string(32)
            reset_request = PasswordResetRequest.objects.create(user=user, email=email, token=token)
            reset_request.send_reset_email()
            messages.success(request, "Reset link send to your mail")
        else:
            messages.error(request, "Email Not Found")
    return render(request, 'authentication/forget-password.html')

def reset_password_view(request, token):
    reset_request = PasswordResetRequest.objects.create(token=token)
    
    if not reset_request or not reset_request.is_valid():
        messages.error(request, 'Invalid or expired reset link')
        return redirect('index')
    
    if request.method == "POST":
        new_password = request.POST['new_password']
        reset_request.user.set_password(new_password)
        reset_request.save()
        messages.success(request, "Password reset Successfully")
        return redirect('login')
    
    return render(request, 'reset_password.html', {'token: token'})
        

def logout_view(request):
    logout(request)  
    messages.success(request, "You have been logout")
    return redirect('index')
         