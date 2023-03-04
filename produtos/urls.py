from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from views import product_list

urlpatterns = [
    
    path('admin/', admin.sites.urls),

    path('product_list/', product_list, name = "listagem")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
