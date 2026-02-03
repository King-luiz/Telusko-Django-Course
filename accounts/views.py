from csv import reader
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages as message

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            message.info(request, "Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')
    

def register(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 ==password2:
            if User.objects.filter(username=username).exists():
                message.info(request, "Username taken")
                
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                message.info(request, "Email taken")
                
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                message.info(request, "User created")
                return redirect('login')
        else:
            message.info(request, "Password not matching")
            
            return redirect('register')
    
    else:
        return render(request, 'register.html')
        
        # Here, you would typically add code to create the user account,
        # validate the data, and handle errors.
        
        # For now, we'll just render the same registration page.
