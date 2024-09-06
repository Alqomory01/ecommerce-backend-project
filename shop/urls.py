from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='ourshop'),
    path('signup/', views.signup, name='myshop'),
    path('login/', views.login_view, name='login'),
    path('order/', views.order, name='order'),
    path('logout/', views.logout, name='logout'),
    
    
]