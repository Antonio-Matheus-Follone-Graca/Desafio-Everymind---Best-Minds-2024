from django import forms

class ProdutoForm(forms.Form):
    # campos do formulário
    # campos com required = True são obrigatórios 
    nome_do_produto = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control mt-2'}), label='Nome do produto')
    codigo_do_produto = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control mt-2'}))
    descricao_do_produto = forms.CharField(required=False,widget=forms.Textarea(attrs={'class': 'form-control mt-2','placeholder':'Campo opcional'}))
    preco_do_produto = forms.DecimalField(required=True, max_digits=10, decimal_places=2,  widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'R$', 'type': 'number', 'step': '0.01'}))

    # validações do formulário
    def clean_codigo_do_produto(self):
        codigo = self.cleaned_data.get('codigo_do_produto')
        if codigo and not codigo.isalnum():
            raise forms.ValidationError("O código do produto deve conter apenas letras e números.")
        return codigo

    def clean_preco_do_produto(self):
        preco = self.cleaned_data.get('preco_do_produto')
        if preco is not None and preco <= 0:
            raise forms.ValidationError("O preço do produto deve ser maior que zero.")
        return preco