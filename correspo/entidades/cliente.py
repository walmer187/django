
class Cliente():
    def __init__(
        self,
        cpf_cnpj,
        nome,
        sobrenome,
        razao_social,
        estado_civil,
        sexo,
        cep,
        logadouro,
        numero,
        bairro,
        complemento,
        cidade,
        estado,
        numero_telefone,
        numero_celular,
        email,
        personalidade_juridica
    ):
        self.__cpf_cnpj = cpf_cnpj
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__razao_social = razao_social
        self.__estado_civil = estado_civil
        self.__sexo = sexo
        self.__cep = cep
        self.__logadouro = logadouro
        self.__numero = numero
        self.__bairro = bairro
        self.__complemento = complemento
        self.__cidade = cidade
        self.__estado = estado
        self.__numero_telefone = numero_telefone
        self.__numero_celular = numero_celular
        self.__email = email
        self.__personalidade_juridica = personalidade_juridica

    @property
    def cpf_cnpj(self):
        return self.__cpf_cnpj

    @cpf_cnpj.setter
    def cpf_cnpj(self, cpf_cnpj):
        self.__cpf_cnpj = cpf_cnpj

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    @property
    def razao_social(self):
        return self.__razao_social

    @razao_social.setter
    def razao_social(self, razao_social):
        self.__razao_social = razao_social

    @property
    def estado_civil(self):
        return self.__estado_civil

    @estado_civil.setter
    def estado_civil(self, estado_civil):
        self.__estado_civil = estado_civil

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, cep):
        self.__cep = cep

    @property
    def logadouro(self):
        return self.__logadouro

    @logadouro.setter
    def logadouro(self, logadouro):
        self.__logadouro = logadouro

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @property
    def complemento(self):
        return self.__complemento

    @complemento.setter
    def complemento(self, complemento):
        self.__complemento = complemento

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado

    @property
    def numero_telefone(self):
        return self.__numero_telefone

    @numero_telefone.setter
    def numero_telefone(self, numero_telefone):
        self.__numero_telefone = numero_telefone

    @property
    def numero_celular(self):
        return self.__numero_celular

    @numero_celular.setter
    def numero_celular(self, numero_celular):
        self.__numero_celular = numero_celular

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def personalidade_juridica(self):
        return self.__personalidade_juridica

    @personalidade_juridica.setter
    def personalidade_juridica(self, personalidade_juridica):
        self.__personalidade_juridica = personalidade_juridica
