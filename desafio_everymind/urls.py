from django.contrib import admin
from django.urls import path, include

# configurando rotas
urlpatterns = [
    path('admin/', admin.site.urls),
    # para os endereços '' manda para o app produtos  arquivo .urls
    path('', include('produtos.urls')),
]
