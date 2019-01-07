from django.db import models
from perfil.models import Perfil

class Modalidade(models.Model):
    descricao = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.descricao

class Ano(models.Model):
    descricao = models.CharField(max_length = 4, unique = True)

    def __str__(self):
        return self.descricao

class Staff(models.Model):
    descricao = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.descricao

class Nivel(models.Model):
    descricao = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.descricao

class Confederacao(models.Model):
    descricao = models.CharField(max_length = 50, unique = True)

    def __str__(self):
        return self.descricao


class Pergunta(models.Model):
    texto = models.TextField()
    respondida = models.BooleanField(default = False)
    correta = models.BooleanField(default = False)
    modalidade = models.ForeignKey('Modalidade', on_delete = models.CASCADE, related_name = 'pergunta')
    ano = models.ForeignKey('Ano', on_delete = models.CASCADE, related_name = 'pergunta')
    confederacao = models.ForeignKey('Confederacao', on_delete = models.CASCADE, related_name = 'pergunta')
    nivel = models.ForeignKey('Nivel', on_delete = models.CASCADE, related_name = 'pergunta')
    staff = models.ForeignKey('Staff', on_delete = models.CASCADE, related_name = 'pergunta')
    respondida = models.ManyToManyField(Perfil, through='Respondida', related_name='pergunta')

    @property
    def alternativa_certa(self):
        for indice, alternativa in enumerate(self.alternativa.all()):
            if alternativa.correta:
                return indice + 1


class Alternativa(models.Model):
    texto = models.TextField()
    correta = models.BooleanField(default = False)
    selecionada = models.BooleanField(default = False)
    pergunta = models.ForeignKey(Pergunta, on_delete = models.CASCADE, related_name = 'alternativa')

class Respondida(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='respondidas')
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='respondida')
    alternativa = models.ForeignKey(Alternativa, on_delete=models.CASCADE, related_name='respondida')

class Comentario(models.Model):
    texto = models.CharField(max_length=500)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='comentario')
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='comentario')
