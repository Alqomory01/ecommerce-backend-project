from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=55)

    def _str_(self):
        return self.name

    

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='product_image')

class CartItem(models.Model):
    # id= models.AutoField(primary_key=True)
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()

    @property
    def total(self):
        return self.product.price * self.quantity

class Cart(models.Model):
    # id = models.AutoField(primary_key=True)
    items = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # amount = models.FloatField()

    @property
    def amount(self):
        return sum(item.total for item in self.items.all)

 


# Create your models here.
