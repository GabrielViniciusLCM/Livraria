
from django.contrib import admin
from django.urls import path
from app_livraria import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # rota/view responsável/nome de referência
    # livraria.com
    path('', views.home, name ='home'),
    # livraria.com/teste
    # path('teste/')
]
