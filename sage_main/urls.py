from django.urls import path
from django.urls.conf import include
from . import views
from django.conf.urls import url

from rest_framework import routers
# router = routers.DefaultRouter()
# router.register(r'products',  views.ProductView, basename='product' )

urlpatterns = [

    # path('home', views.home, name='exam-home'),
    path('home', views.home, name='home'),
    # url(r'^api/', include(router.urls))
    # path('products/', views.ProductView.as_view({'get': 'list'}), name='product-get'),
    # path('product/save', views.ProductView.as_view({'post': 'list'}), name='product-save'),
    # path('login/', views.student_login, name='student-login'),
]