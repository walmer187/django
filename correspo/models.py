from django.db import models


# Create your models here.
class Cliente(models.Model):
    ESTADO_CHOICES = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins")
    )
    ESTADO_CIVIL_CHOICES = (
        ("Solteiro", "Solteiro(a)"),
        ("Casado", "Casado(a)")
    )
    SEXO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("N", "Não declarar")
    )
    PERSONALIDADE_CHOICES = (
        ("PF", "Pessoa Física"),
        ("PJ", "Pessoa Jurídica")
    )
    cpf_cnpj = models.CharField(
        primary_key=True,
        max_length=14,
        null=False,
        blank=False
    )

    nome = models.CharField(
        max_length=100,
    )

    sobrenome = models.CharField(
        max_length=100,
    )

    razao_social = models.CharField(
        max_length=255,
        blank=True
    )

    estado_civil = models.CharField(
        max_length=20,
        choices=ESTADO_CIVIL_CHOICES,
    )

    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICES,
        blank=True

    )

    cep = models.CharField(
        max_length=20,
        blank=True
    )

    logadouro = models.CharField(
        max_length=100,
    )

    numero = models.CharField(
        max_length=5
    )

    bairro = models.CharField(
        max_length=100,
        blank=True
    )

    complemento = models.CharField(
        max_length=100,
        blank=True
    )

    cidade = models.CharField(
        max_length=100
    )

    estado = models.CharField(
        max_length=2,
        choices=ESTADO_CHOICES,
        blank=False
    )

    numero_telefone = models.CharField(
        max_length=20,
        blank=True
    )

    numero_celular = models.CharField(
        max_length=20
    )

    email = models.EmailField(
        blank=True
    )

    personalidade_juridica = models.CharField(
        max_length=2,
        choices=PERSONALIDADE_CHOICES,
        blank=False
    )

    def __str__(self):
        return (self.cpf_cnpj,
                self.nome,
                self.sobrenome,
                self.razao_social,
                self.estado_civil,
                self.sexo,
                self.cep,
                self.logadouro,
                self.numero,
                self.bairro,
                self.complemento,
                self.cidade,
                self.estado,
                self.numero_telefone,
                self.numero_celular,
                self.email,
                self.personalidade_juridica
                )
