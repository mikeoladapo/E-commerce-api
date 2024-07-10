from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    phonenumber = models.CharField(max_length=12 )
    shipping_address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics',blank=True,null=True)
    @property
    def username(self):
        return self.user.username

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    about = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_picture = models.ImageField(upload_to='product_pics',blank=True,null=True)
    @property
    def category_name(self):
        return self.category.name 

    def __str__(self):
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.product.name
    @property
    def total_amount(self):
        self.total_price = self.quantity * self.price
        return self.total_price
    @property
    def product_name(self):
        return self.product.name 

        

