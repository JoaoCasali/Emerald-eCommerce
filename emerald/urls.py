from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Auth/', include('usuarios.urls')),
    path('Produtos/', include('produtos.urls')),
    path('', include('main.urls')),
]

# handler404 = "main.views.PageNotFound"