from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def landing_page(request):
    return render(request, "landing.html")

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request, 'login.html')

def post_register(request):
    request.POST
    errorsFromValidator = User.objects.userValidator(request.POST)
    if len(errorsFromValidator)>0:
        for key, value in errorsFromValidator.items():
            messages.error(request, value, extra_tags= "register")
        return redirect("/register")

    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    print("password hash below")
    print(pw_hash)
    newUser = User.objects.create(firstname = request.POST['firstname'], lastname = request.POST['lastname'], username = request.POST['username'], password = pw_hash, confirm_password = pw_hash)
    print(request.POST)
    print(newUser)
    request.session['loggedinId'] = newUser.id
    return redirect('/user_page')

def post_login(request):
    request.POST
    errorsFromValidator = User.objects.loginValidator(request.POST)
    if len(errorsFromValidator)>0:
        for key, value in errorsFromValidator.items():
            messages.error(request, value, extra_tags= "login")
        return redirect("/login")

    user = User.objects.get(username = request.POST['username'])
    request.session['loggedinId'] = user.id
    print('Login Successful')
    return redirect ('/user_page')

def user_page(request):
    if 'loggedinId' not in request.session:
        return redirect('login')
    loggedinUser = User.objects.get(id = request.session['loggedinId'])
    context = {
        "loggedinUser": loggedinUser,
        
    }
    return render(request, "user_page.html", context)
def champions_page(request):
    if 'loggedinId' not in request.session:
        return redirect('login')
    loggedinUser = User.objects.get(id = request.session['loggedinId'])
    context = {
        "loggedinUser": loggedinUser,
        
    }
    return render(request, "champions.html", context)

def logout(request):
    request.session.clear()
    return redirect('/login')