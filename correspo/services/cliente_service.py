from correspo.models import Cliente


def listar_clientes():
    clientes = Cliente.objects.all()
    return clientes


def listar_cliente_cpf_cnpj(cpf_cnpj):
    cliente = Cliente.objects.get(cpf_cnpj=cpf_cnpj)
    return cliente


def remover_cliente(cliente):
    cliente.delete()


def cadastrar_cliente(cliente):

    Cliente.objects.create(
        cpf_cnpj=cliente.cpf_cnpj,
        nome=cliente.nome,
        sobrenome=cliente.sobrenome,
        razao_social=cliente.razao_social,
        estado_civil=cliente.estado_civil,
        sexo=cliente.sexo,
        cep=cliente.cep,
        logadouro=cliente.logadouro,
        numero=cliente.numero,
        bairro=cliente.bairro,
        complemento=cliente.complemento,
        cidade=cliente.cidade,
        estado=cliente.estado,
        numero_telefone=cliente.numero_telefone,
        numero_celular=cliente.numero_celular,
        email=cliente.email,
        personalidade_juridica=cliente.personalidade_juridica
    )


def editar_cliente(cliente, cliente_novo):
    print(cliente_novo.cpf_cnpj)
    print(cliente.nome)
    cliente.cpf_cnpj = cliente_novo.cpf_cnpj,
    cliente.nome = cliente_novo.nome,
    cliente.sobrenome = cliente_novo.sobrenome,
    cliente.razao_social = cliente_novo.razao_social,
    cliente.estado_civil = cliente_novo.estado_civil,
    cliente.sexo = cliente_novo.sexo,
    cliente.cep = cliente_novo.cep,
    cliente.logadouro = cliente_novo.logadouro,
    cliente.numero = cliente_novo.numero,
    cliente.bairro = cliente_novo.bairro,
    cliente.complemento = cliente_novo.complemento,
    cliente.cidade = cliente_novo.cidade,
    cliente.estado = cliente_novo.estado,
    cliente.numero_telefone = cliente_novo.numero_telefone,
    cliente.numero_celular = cliente_novo.numero_celular,
    cliente.email = cliente_novo.email,
    cliente.personalidade_juridica = cliente_novo.personalidade_juridica,
    cliente.save(force_update=True)
