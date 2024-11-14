from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ourshop/<str:model_name>/<int:pk>/', views.shop, name='ourshop'),
    path('add/', views.add_cart, name='addcart'),
    path('signup/', views.signup, name='myshop'),
    path('login/', views.login_view, name='login'),
    path('order/', views.order, name='order'),
    path('logout/', views.logout, name='logout'),
    path('cart/', views.cart, name="cart"),
    
]