from django.contrib.auth import forms
from django import forms
from rest_framework import serializers
from . models import *
from site_admin.models import *
from site_admin.models import Admin
from users.models import Profile, Customer







class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'image')


class ProductSerializer(serializers.ModelSerializer):

    # category = CategorySerializer(many=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'short_description', 'description', 'image', 'featured_image1', 'featured_image2','featured_image3', 'price','deleted_price', 'in_stock', 'is_favorite', 'is_recommended', 'is_popular','category', 'date_added')
        # expandabl



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

# class CustomerProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user', 'slug', 'address', 'profile_pic', 'mobile')





class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'product', 'author', 'content', 'rating', 'date_added')

