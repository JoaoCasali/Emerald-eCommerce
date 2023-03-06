from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.product_list, name = "listagem")
    path('Cadastro/', views.Cadastro, name='cadastroProduto'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
