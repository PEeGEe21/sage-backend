from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import View
from rest_framework import routers

from users import views as users_views
from sage_main import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



router = routers.DefaultRouter()
router.register(r'products',  views.ProductView, 'product' )
router.register(r'category',  views.CategoryView, 'category' )
router.register(r'reviews',  views.ReviewView, 'reviews' )
router.register(r'register',  views.RegisterView, 'register' )


urlpatterns = [
    path('super-admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    # path('token/', views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),

]


urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)