import data
from data import *

class Produto:

    def __init__(self, nome, preco):

        self.__id = None
        self.nome = nome
        self.preco = preco


    def __str__(self):

        return f'ID: {self.id} | NOME: {self.nome} | PREÇO: {self.preco}'



    @property #Melhor para retorno mais seguro de "_preço"
    def preco(self):
        return self._preco


    @preco.setter #importante pra garantir de forma ideal a troca do "_preço"
    def preco(self, valor):


        try:
            valor = float(valor)

        except ValueError:
            raise ValueError('Preço inválido')

        if valor < 0:
            raise ValueError('Não é possível enviar preços negativos.')

        self._preco = valor



    @property #@property e id.setter são fundamentais para a criação do atributo "id". Não remover.
    def id(self):
        return self.__id


    @id.setter
    def id(self, valor):

        if self.id is None:
            self.__id = valor

        else:
            raise ValueError('ID já atribuído')


prod = Produto('Teste de negativo', '-1')




print(prod)