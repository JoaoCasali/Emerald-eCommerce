from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('Cadastro/', views.CadastroProduto, name='cadastroProduto'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
