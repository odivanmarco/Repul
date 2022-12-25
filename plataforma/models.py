from django.db import models


class Imagem(models.Model):
    img = models.ImageField(upload_to='img')

    def __str__(self) -> str:
        return self.img.url


class Republica(models.Model):
    nome_republica = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    numero_da_republica = models.PositiveIntegerField()
    valor = models.PositiveIntegerField()
    quantidade_de_quartos = models.PositiveIntegerField()
    quantidade_de_banheiros = models.PositiveIntegerField()
    quantidade_de_vagas_garagem = models.PositiveIntegerField()
    regras_da_republica = models.TextField(max_length=2000)
    contato = models.CharField(max_length=20)
    nome_do_anunciante = models.CharField(max_length=60)
    fotos = models.ManyToManyField(Imagem)
    descricao = models.TextField(max_length=2000)


class Contato(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=254)
    telefone = models.CharField(max_length=20)
    mensagem = models.TextField()
    def __str__(self) :
        return self.name