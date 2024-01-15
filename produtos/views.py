from django.shortcuts import render

# Create your views here.

# Funções que realizam o crud

def index(request):
    # retorna para a rota index.html
    return render(request,'index.html')
