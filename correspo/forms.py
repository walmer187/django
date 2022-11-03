from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'cpf_cnpj',
            'nome',
            'sobrenome',
            'razao_social',
            'estado_civil',
            'sexo',
            'cep',
            'logadouro',
            'numero',
            'bairro',
            'complemento',
            'cidade',
            'estado',
            'numero_telefone',
            'numero_celular',
            'email',
            'personalidade_juridica'
        ]
