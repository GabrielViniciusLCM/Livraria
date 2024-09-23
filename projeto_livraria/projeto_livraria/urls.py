
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # rota/view responsável/nome de referência
    # livraria.com
    path(''),
    # livraria.com/teste
    path('teste/')
]
