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
from rest_framework import permissions

from .serializer import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated




class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = changePasswordSerializer



    