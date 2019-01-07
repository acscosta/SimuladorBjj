from django.core.management.base import BaseCommand, CommandError
from questoes.models import Modalidade, Ano, Staff, Confederacao, Nivel 

class Command(BaseCommand):
    help = 'script para popular as tabelas de dominio'

    modalidades = ['JIU JITSU']
    staffs = ['STAFF BJJ']
    anos = ['2018']
    confederacaos = ['CBJJ', 'SJJSAF']
    niveis =['Nível Fácil','Nível Médio', 'Nível Superior']

    def handle(self, *args, **options):
        self.popular_tabelas()

    def popular_tabelas(self):
        self.popular_tabela(Modalidade, self.modalidades)
        self.popular_tabela(Ano, self.anos)
        self.popular_tabela(Staff, self.staffs)
        self.popular_tabela(Nivel, self.niveis)
        self.popular_tabela(Confederacao, self.confederacaos)
        self.stdout.write('Registros inseridos com sucesso!')

    def popular_tabela(self, objeto, lista):
        for descricao in lista:
            novo_objeto = self.criar_objeto(objeto, descricao)
            try:
                novo_objeto.save()
            except:
                self.stdout.write('O registro "%s" já existe na base de dados' % descricao)

    def criar_objeto(self, objeto, descricao):
        if (objeto.__name__ == 'Modalidade'):
            return Modalidade(descricao = descricao)
        if (objeto.__name__ == 'Ano'):
            return Ano(descricao = descricao)
        if (objeto.__name__ == 'Nivel'):
            return Nivel(descricao = descricao)
        if (objeto.__name__ == 'Confederacao'):
            return Confederacao(descricao = descricao)
        if (objeto.__name__ == 'Staff'):
            return Staff(descricao = descricao)