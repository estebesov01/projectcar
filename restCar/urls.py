from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as up

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/cars/', include('cars.urls')),
    path('api/v1/base-auth', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth_token/', include('djoser.urls.authtoken')),
]
urlpatterns += up
