from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.name

    

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    image = models.ImageField(upload_to='product_image', blank=True, null=True)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    @property
    def total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)

    @property
    def amount(self):
        total_amount = sum( item.total for item in self.items.all())
        return total_amount

    def __str__(self):
        return f"{self.user.username} - Total: {self.amount}"

    class Meta:
        unique_together = ("user",)


class paystack(models.Model):
        id = models.AutoField(primary_key=True)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        amount = models.FloatField()
        reference_id = models.CharField(max_length=55 )
        status = models.CharField(max_length=15, default="processing")
        date = models.DateTimeField(auto_now_add=True)

 

        def __str__(self):
            return f"{self.user.username} payment of {self.amount}"
class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    reference = models.CharField(max_length=10)
    status = models.CharField(max_length=10, default='processing')
    time = models.DateTimeField(auto_now_add=True)


# session based token
# javscript web token jwb
# All ought Authentication
    # social Authentication

# class CartItem(models.Model):
    # id= models.AutoField(primary_key=True)
    # product =models.ForeignKey(Product, on_delete=models.CASCADE)
    # quantity = models.IntegerField(default=1)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # total = models.FloatField()

    # @property
    # def total(self):
    #     return self.product.price * self.quantity
    

        
# class Cart(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Cart ({self.user.username})"

#     def add_item(self, product, quantity=1):
#         cart_item, created = CartItem.objects.get_or_create(cart=self, product=product)
#         cart_item.quantity += quantity
#         cart_item.save()
#         return cart_item

# class Cart(models.Model):
#     id = models.AutoField(primary_key=True)
    # items = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # amount = models.FloatField()

    # @property
    # def amount(self):
    #     cost = self.items.total
    #     return sum(cost for cost in cost.all)
    
    # def add_item(self, product, quantity=1):
    #     cart_user, created = CartItem.objects.get_or_create(cart=self, product=product)
    #     cart_user.quantity += quantity
    #     cart_user.save()
    #     return cart_user

    # @property
    # def amount(self):
    #     cost = self.items.total
    #     return sum(cost for cost in cost.all)
    
# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     total = models.FloatField()

#     @property
#     def total(self):
#         return self.product.price * self.quantity
    


# Create your models here.
