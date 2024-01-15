from django.shortcuts import render,redirect,get_object_or_404
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
        # por padrão o banco de dados do Django aceita , em decimal e já converte para . por isso não fiz validação
        if form.is_valid():
           # insert do produto 
            novo_produto = Produtos(nome_produto=nome_produto, codigo_produto=codigo_produto, descricao_produto=descricao_produto, preco_produto=preco_produto)
            novo_produto.save()
            # redirecionando para a index
            return redirect('index')
    
    return render(request,'cadastrar_produto.html', {'form':form})

def excluir_produto(request, id_produto):
    '''
        Deleta um produto ao clicar no deletar produto
    '''
    # procurando id do produto
    produto = get_object_or_404(Produtos, id=id_produto)
    # Verifica se o método da requisição é POST (para evitar exclusões acidentais)
    # Exclui o produto
    produto.delete()

    # Redireciona para o index
    return redirect('index')

def editar_produto(request, id_produto):
    # pegando id do produto 
    produto = get_object_or_404(Produtos, id=id_produto)
    # se clicou para editar
    if request.method == 'POST':
        # Preencha o formulário com os dados enviados no POST e os valores existentes do produto
        form = ProdutoForm(request.POST)
        if form.is_valid():
            # pegando os valores do formulário e atualizando
            produto.nome_produto = request.POST.get('nome_do_produto')
            produto.codigo_produto = request.POST.get('codigo_do_produto')
            produto.descricao_produto = request.POST.get('descricao_do_produto')
            produto.preco_produto = request.POST.get('preco_do_produto')
            # atualizando produto 
            produto.save()
            return redirect('index')
    
    # senão clicou no atualizar ou está indo para a página
    else:
        form = ProdutoForm(initial={'nome_do_produto': produto.nome_produto, 'codigo_do_produto': produto.codigo_produto, 'descricao_do_produto': produto.descricao_produto, 'preco_do_produto': produto.preco_produto} )
        
    return render(request, 'editar_produto.html', {'form': form, 'produto': produto})


    
    