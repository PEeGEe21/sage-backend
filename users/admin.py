from django.contrib import admin
from .models import Profile, Customer

# Register your models here.
admin.site.register(Customer)
admin.site.register(Profile)