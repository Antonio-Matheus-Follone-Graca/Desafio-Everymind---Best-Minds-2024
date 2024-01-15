from django.shortcuts import render,redirect
from .forms import ProdutoForm
from .models import Produtos
# Create your views here.

# Funções que realizam o crud

def index(request):
    '''
        Página index que mostra todos os produtos
    '''
    # seleciona todos os produtos
    todos_produtos = Produtos.objects.all()
    # retorna para a rota index.html
    return render(request,'index.html', {'dados_produtos': todos_produtos})

def criar_produto(request):
    '''
        Página de criar produto
    '''
    form = ProdutoForm()
    if request.method == 'POST':
        # pega os dados do formulário e repassa para a classe ProdutoForm
        form= ProdutoForm(request.POST)
        #pegando do formulário e guardando em variaveis
        nome_produto = request.POST.get('nome_do_produto')
        codigo_produto = request.POST.get('codigo_do_produto')
        descricao_produto = request.POST.get('descricao_do_produto')
        preco_produto = request.POST.get('preco_do_produto')
        # por padrão o banco de dados do Djando aceita , em decimal e já converte para . por isso não fiz validação
        if form.is_valid():
           # insert do produto 
            novo_produto = Produtos(nome_produto=nome_produto, codigo_produto=codigo_produto, descricao_produto=descricao_produto, preco_produto=preco_produto)
            novo_produto.save()
            # redirecionando para a index
            return redirect('index')
    
    return render(request,'cadastrar_produto.html', {'form':form})
