from rest_framework import serializers
from .models import Profile,Product,Category,Order

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id","username","date_of_birth","phonenumber","shipping_address","profile_picture")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id","name","about","price","category_name")

class CategorySerializer(serializers.ModelSerializer):
   class Meta:
    model = Category
    fields = ('id', 'name')
   
    
class CategoryDetailSerializer(serializers.ModelSerializer):
  products = serializers.SerializerMethodField()

  def get_products(self, obj):
    return ProductSerializer(obj.product_set.all(), many=True).data

  class Meta:
    model = Category
    fields = ('id', 'name', 'products')
  
class OrderSerializer(serializers.ModelSerializer):
   class Meta:
      model = Order
      fields = ("id","product_name","status","created_at","quantity","total_amount")

