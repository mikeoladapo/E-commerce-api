from django.contrib import admin
from .models import Profile,Product,Category,Order
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
