from django.db import models

# Create your models here.

# Tabela com o banco de dados 

'''
    Campos 
        • Nome do produto (String)
        • Código do produto (String)
        • Descrição do produto (TextField)
        • Preço do produto (Decimal)
'''

class Produtos(models.Model):
    nome_produto = models.CharField(max_length =200, null= False, blank=False) # campo não pode aceitar valor nulo e não pode ficar vazio. É obrigatório o preenchimento
    codigo_produto = models.CharField(max_length =200, null= False, blank=False) # campo não pode aceitar valor nulo e não pode ficar vazio. É obrigatório o preenchimento
    descricao_produto = models.TextField( null = True, blank = True)  # campo pode aceitar nulo e não é obrigatório o preenchimento
    preco_produto= models.DecimalField(max_digits=10, decimal_places=2,null= False, blank=False) # campo não pode aceitar valor nulo e não pode ficar vazio. É obrigatório o preenchimento