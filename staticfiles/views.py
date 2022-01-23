import django
from django.shortcuts import render, redirect, reverse, get_object_or_404, resolve_url
from json.encoder import JSONEncoder
from django.core import paginator
from django.contrib import messages
# from exam.models import Student, Paper, Teacher, Exam, Grade
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from exam.models import models
from django.db import models
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, response
from rest_framework import permissions
from rest_framework.views import APIView
from .models import Product
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.decorators import login_required
from rest_framework import serializers
from .serializer import *
from sage_main import serializer
from rest_framework import viewsets
from django.contrib.auth.models import Group
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated



# Create your views here.
def home(request):
    return render(request, 'sage_main/base.html')


class ProductView(viewsets.ModelViewSet):
# class ProductView(viewsets.ViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'in_stock', 'is_popular', 'is_recommended']
    # permission_classes = [IsAuthenticated]



class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ReviewView(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()


class RegisterView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class ProfileView(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = Profile.objects.all()



    # def post(self, request):
        
    #     # queryset = Customer.objects.all()

    #     if request.method=='POST':
    #         CustomerSerializerForm = CustomerSerializer(data=request.data)
    #         print('stoppinggg here')
    #         # customerSerializerForm
    #         # studentForm=forms.StudentForm(request.POST,request.FILES)
    #         if CustomerSerializerForm.is_valid():
    #             my_user_group = Group.objects.get_or_create(name='Customers')
    #             user=CustomerSerializerForm.save()
    #             my_user_group[0].user_set.add(user)
    #             user.set_password(user.password)
    #             user.save()
    #             return Response(user.data)
    #             # student=studentForm.save(commit=False)
    #             # student.user=user
    #             # student.save()
        
    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Customer.objects.all()


    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return User.objects.all()
    
    # def post(self, request):
    #         # if request.method == 'POST':
    #             # serializer = ProductSerializer(data=request.data)
    #             # if serializer.is_valid(raise_exception=True):
    #             #     serializer.save()
    #             #     return Response(serializer.data)

    #     if request.method=='POST':
    #         userSerializerForm = UserSerializer(data=request.data)
    #         # customerSerializerForm
    #         # studentForm=forms.StudentForm(request.POST,request.FILES)
    #         if userSerializerForm.is_valid():
                
    #             user=userSerializerForm.save()
    #             my_user_group = Group.objects.get_or_create(name='Customers')
    #             my_user_group[0].user_set.add(user)
    #             user.set_password(user.password)
    #             user.save()
    #             # student=studentForm.save(commit=False)
    #             # student.user=user
    #             # student.save()
                
    #         return HttpResponseRedirect('studentlogin')



    # def get(self, request):
    #     product = Product.objects.all()
    #     return Response(product)

    # def post(self, request):
        # if request.method == 'POST':
        #     serializer = ProductSerializer(data=request.data)
        #     if serializer.is_valid(raise_exception=True):
        #         serializer.save()
        #         return Response(serializer.data)