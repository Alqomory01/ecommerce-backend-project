from django.shortcuts import render, get_list_or_404
from django.contrib.auth.models import User
from .models import Product, Category
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {'products':products, 'categories': categories} )



def shop(request):
    # product = get_list_or_404()
    return render(request, 'shop.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:   #and len(password1) > 8
            user = User.objects.create_user(username, email, password1)
            user.save()
            auth.login(request, user)
            return redirect('home')
        return render(request, 'signin.html', {'failure': 'Wrong Password. please login'})
    return render(request, 'login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user)
            auth.login(request, user)
            # print("user login")
            # login(request, user)
            return redirect('home')
        else:
            error_message = 'invalid username or password'
            return render(request, 'badsignup.html', {'error_message': error_message})
    return render(request, 'signin.html')
 
def logout(request):
    auth.logout(request)
    return redirect('home')

def email_req(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email)
        if user.exists():
            return render(request, 'email_req.html', {'success': 'An email has been sent to the provided address'})
        else:
            return render(request, 'email_req.html', {'error': 'email does no exist in our system'})




def order(request):
    return render(request, 'order.html')

def logout(request):
    return render(request, 'logout.html')

# Create your views here.
