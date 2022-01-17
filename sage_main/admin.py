from django.contrib import admin
from .models import Category, Product, Review, Cart, Order
from django.contrib.auth.models import Group



# admin.site.register(Exam)
admin.site.site_header = 'Sage Online Market system'
admin.site.site_title = 'Sage Online Market system'


# admin.register(Product)
admin.site.register(Product)
# class ProductAdmin(admin.ModelAdmin):
# # What information to display
#     list_display = '__all__'
#     # What information can you click to enter the edit page
#     list_display_links = ('id', 'name')


# class ProductAdmin(admin.ModelAdmin):
#     list_display =('pk', n)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(Order)


# admin.site.unregister(Group)

