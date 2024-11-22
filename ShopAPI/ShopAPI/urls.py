from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ShopAPIApp.urls')),
    #path('api/', include('ShopAPIApp.urls')),# Подключение маршрутов приложения
]