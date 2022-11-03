from django.shortcuts import redirect, render

from .entidades import cliente
from .forms import ClienteForm
from .services import cliente_service


# Create your views here.
def my_view(request):
    return render(request, 'correspo/home.html', context={
        'name': 'Walmer Souza'
    })


def listar_clientes(request):
    clientes = cliente_service.listar_clientes()
    return render(request, 'clientes/listar_clientes.html', {
        'clientes': clientes
    })


def inserir_clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            # form.save()
            cpf_cnpj = request.POST.get['cpf_cnpj']
            nome = form.cleaned_data['nome']
            sobrenome = form.cleaned_data['sobrenome']
            razao_social = form.cleaned_data['razao_social']
            estado_civil = form.cleaned_data['estado_civil']
            sexo = form.cleaned_data['sexo']
            cep = form.cleaned_data['cep']
            logadouro = form.cleaned_data['logadouro']
            numero = form.cleaned_data['numero']
            bairro = form.cleaned_data['bairro']
            complemento = form.cleaned_data['complemento']
            cidade = form.cleaned_data['cidade']
            estado = form.cleaned_data['estado']
            numero_telefone = form.cleaned_data['numero_telefone']
            numero_celular = form.cleaned_data['numero_celular']
            email = form.cleaned_data['email']
            personalidade = form.cleaned_data['personalidade_juridica']

        cliente_novo = cliente.Cliente(
            cpf_cnpj=cpf_cnpj,
            nome=nome,
            sobrenome=sobrenome,
            razao_social=razao_social,
            estado_civil=estado_civil,
            sexo=sexo,
            cep=cep,
            logadouro=logadouro,
            numero=numero,
            bairro=bairro,
            complemento=complemento,
            cidade=cidade,
            estado=estado,
            numero_telefone=numero_telefone,
            numero_celular=numero_celular,
            email=email,
            personalidade_juridica=personalidade
        )
        cliente_service.cadastrar_cliente(cliente_novo)
        return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/form_clientes.html', {'form': form})


def listar_cliente_cpf_cnpj(request, id):
    # cliente = Cliente.objects.get(cpf_cnpj=id)
    cliente = cliente_service.listar_cliente_cpf_cnpj(id)
    return render(request, 'clientes/lista_cliente.html', {'cliente': cliente})


def editar_cliente(request, id):
    # cliente = Cliente.objects.get(cpf_cnpj=id)
    cliente_antigo = cliente_service.listar_cliente_cpf_cnpj(id)
    form = ClienteForm(request.POST or None, instance=cliente_antigo)
    if form.is_valid():
        cpf_cnpj = form.cleaned_data['cpf_cnpj']
        nome = form.cleaned_data['nome']
        sobrenome = form.cleaned_data['sobrenome']
        razao_social = form.cleaned_data['razao_social']
        estado_civil = form.cleaned_data['estado_civil']
        sexo = form.cleaned_data['sexo']
        cep = form.cleaned_data['cep']
        logadouro = form.cleaned_data['logadouro']
        numero = form.cleaned_data['numero']
        bairro = form.cleaned_data['bairro']
        complemento = form.cleaned_data['complemento']
        cidade = form.cleaned_data['cidade']
        estado = form.cleaned_data['estado']
        numero_telefone = form.cleaned_data['numero_telefone']
        numero_celular = form.cleaned_data['numero_celular']
        email = form.cleaned_data['email']
        personalidade = form.cleaned_data['personalidade_juridica']

        cliente_novo = cliente.Cliente(
            cpf_cnpj=cpf_cnpj,
            nome=nome,
            sobrenome=sobrenome,
            razao_social=razao_social,
            estado_civil=estado_civil,
            sexo=sexo,
            cep=cep,
            logadouro=logadouro,
            numero=numero,
            bairro=bairro,
            complemento=complemento,
            cidade=cidade,
            estado=estado,
            numero_telefone=numero_telefone,
            numero_celular=numero_celular,
            email=email,
            personalidade_juridica=personalidade
        )
        cliente_service.editar_cliente(cliente_antigo, cliente_novo)
        return redirect('listar_clientes')
    return render(request, 'clientes/form_clientes.html', {'form': form})


def remover_cliente(request, id):
    cliente = cliente_service.listar_cliente_cpf_cnpj(id)

    if request.method == "POST":
        # cliente.delete()
        cliente_service.remover_cliente(cliente)
        return redirect('listar_clientes')
    return render(request,
                  'clientes/confirma_exclusao.html',
                  {'cliente': cliente})
