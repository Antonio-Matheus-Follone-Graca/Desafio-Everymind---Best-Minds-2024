from django.urls import path
# importando views.py do app produtos
from . import views
# configurando rotas
urlpatterns = [
    # chama a função index de views.py do app / pasta produtos
    path('', views.index, name='index'),
    path('criar_produto/', views.criar_produto, name="criar_produto"), # name é o nome para chamada da rota
]
