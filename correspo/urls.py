from django.urls import path

from correspo.views import (editar_cliente, inserir_clientes,
                            listar_cliente_cpf_cnpj, listar_clientes, my_view,
                            remover_cliente)

urlpatterns = [
    path('sobre/', my_view),
    path('clientes/listar/', listar_clientes, name='listar_clientes'),
    path('clientes/cadastrar/', inserir_clientes, name='inserir_clientes'),
    path('clientes/listar/<id>', listar_cliente_cpf_cnpj,
         name='listar_cliente_cpf_cnpj'),
    path('clientes/editar/<id>', editar_cliente, name='editar_cliente'),
    path('clientes/remover/<id>', remover_cliente, name='remover_cliente'),
]
