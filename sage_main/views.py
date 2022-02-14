from locale import currency
from statistics import mode
import django
from django.conf import settings
import stripe
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
from .models import Product, Order
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.decorators import login_required
from rest_framework import serializers
from .serializer import *
from sage_main import serializer
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from django.contrib.auth.models import Group
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

stripe.api_key = settings.STRIPE_SECRET_KEY

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



@api_view(['POST'])
def test_payment(request):
    data = request.data
    print(data, "dataaaaaaaa")

    source = data["tokenId"]
    amount = data["amount"]    
    # billing_details = data["billingAddress"]

    # address = data["billing_details"].address
    # state= data["address_city"]
    # country= data["address_country"]
    # city= data["address_line1"]

    # address = (state + "," + country + "," + city)
    description = data["description"]
    print(description, "description")
    # print(billing_details, "billing_details")
    # print(source, "sourceeeeee")
    # print(billing_details, "billing_details")
    # print(address, "adresssssss")

    try:

        print("workinggg")
        test_payment_intent = stripe.Charge.create(
            source= source,
            amount= amount,
            description = description,
            currency="usd",
            

            )
        amount = test_payment_intent["amount"] 
        orderstatus = test_payment_intent["status"]
        paid = test_payment_intent["paid"]
        payment_method = test_payment_intent["payment_method"]

        user = test_payment_intent["billing_details"].name
        city = test_payment_intent["billing_details"].address.city
        country = test_payment_intent["billing_details"].address.country
        line1 = test_payment_intent["billing_details"].address.line1

        address = (line1 + " , " + country + " , " + city)

        print(user, "user")

        print(amount, "amount")
        print(address, "addresssssss")
        print(orderstatus, "orderstatus")
        print(paid, "paid")
        print(payment_method, "payment_method")
        print(description, "description")
        print(test_payment_intent, "test_payment_intent")

        # order = Order.objects.create(
        #     user=user,

        #     ordered_products='egusi soup',

        #     amount=amount,
        #     address=address,
        #     orderstatus=orderstatus,
        #     paid=paid,
        #     payment_method=payment_method,
        #     description=description
        # )
        # order.save()
        # print(order, "order")

        # test_payment_intent = stripe.PaymentIntent.create(amount=1000, currency='pln', payment_method_types= ['card'],receipt_email='test@example.com')
        

        return Response(status=status.HTTP_200_OK)
    except:
            return Response({
                'error': 'Something went wrong'
            }, status=status.HTTP_200_OK,
            )


class StripeCheckoutView(APIView):
    def post(self, request):
        try:
            checkout_session= stripe.checkout.Session.create(
                line_items=[{
                    'price': 'price_xxxx',
                    'quantity': 1,
                },],
                payment_method_types= ['card',],
                mode = 'payment',
                success_url=settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url=settings.SITE_URL + '/?canceled=true',

            )
            return redirect(checkout_session.url)
        except:
            return Response({
                'error': 'Something went wrong'
            }, status=status.HTTP_200_OK,
            )
                

    

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