from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from .models import Product, Category, Cart, CartItem
from django.contrib import auth
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .paystack import paystack

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {'products':products, 'categories': categories} )


def shop(request, model_name, pk):
    product = None
    if model_name =='product':
        product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    
    return render(request, 'shop.html', context)

def Paystack(request, user_id, cart_id):
    try:
        user = get_object_or_404(User, pk=user_id)
        if user.is_authenticated():
            email = user.email
            cart = Cart.objects.filter(user=user_id)
            amount = cart.amount
    except User.DoesNotExist:
        return Http404
   
    
    accept = paystack()
    return accept

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

def add_cart(request):
    
    product = get_object_or_404(Product, pk=pk)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if cart_item in cart.items.all():
        cart_item.quantity += 1
    else:
        cart.items.add(cart_item)
    cart_item.save()
    return redirect('cart')

def update_cartitem(request, pk, data):
    item = get_object_or_404(CartItem, pk=pk)
    new = item.save(data=data)
    return HttpResponse(201)

def delete_cartitem(request, pk):
    item = get_object_or_404(CartItem, pk=pk)
    item.delete()
    return redirect('cart')

def cart(request):
    user = request.user.id
    if user:
        cart = Cart.objects.filter(user=user).first()
        items = CartItem.objects.filter(cart=cart)  
        return render(request, "cart.html", {"carts": cart, "items": items})
    return render(request, "cart.html")


# @require_http_methods(["GET", "POST"])
# def payment(request, user_id):
#     user = get_object_or_404(User, id=user_id)

#     if request.user.id != user_id:
#         return HttpResponse("Unauthorized", status=403)

#     try:
#         cart = Cart.objects.get(user=user)
#     except Cart.DoesNotExist:
#         return HttpResponse("No cart found for this user", status=404)

#     if request.method == "POST":
#         try:
#             amount = cart.amount
#             email = user.email

#             accept = paystack(email=email, amount=amount)
#             url = accept["authorization_url"]
#             reference = accept["reference_id"]

#             Payment.objects.create(user=user, amount=amount, reference=reference)
#             cart.delete()

#             return redirect(url)

#         except Exception as e:
#             return HttpResponse(f"An error occurred: {str(e)}", status=500)

#     else:  # GET request
#         payment_url = reverse("payment", args=[user_id])
#         csrf_token = get_token(request)
#         return HttpResponse(
#             f"""
#             <html>
#                 <body>
#                     <h1>Proceed to Payment</h1>
#                     <p>Cart total: ${cart.amount}</p>
#                     <form action="{payment_url}" method="post">
#                         <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
#                         <input type="submit" value="Pay Now">
#                     </form>
#                 </body>
#             </html>
#             """
#         )




    # cart.save()
    # return HttpResponse(201)


# def cart(request):
#     user request.user.id

# def update_cartitem(request, pk):
#     item = get_object_or_404(CartItem, pk=pk)
    # new = item.update(data=data)

    return HttpResponse(201)

def delete_cartitem(request,pk):
    item = get_object_or_404(CartItem, pk=pk)
    item.delete()
    return HttpResponse(201)
def order(request):
    return render(request, 'order.html')

def logout(request):
    return render(request, 'logout.html')

# Create your views here.
