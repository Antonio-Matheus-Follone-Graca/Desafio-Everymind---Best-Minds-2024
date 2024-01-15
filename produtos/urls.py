from django.urls import path
# importando views.py do app produtos
from . import views
# configurando rotas
urlpatterns = [
    # chama a função index de views.py do app / pasta produtos
    path('', views.index),
]
