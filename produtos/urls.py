from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('Listagem/', views.product_list, name = "listagemProduto"),
    path('Cadastro/', views.Cadastro, name='cadastroProduto'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
