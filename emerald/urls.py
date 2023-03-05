from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    path('auth/', include('produtos.urls')),
    path('', include('main.urls')),
]
