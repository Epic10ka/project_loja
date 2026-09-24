import data
from data import *

class Produto:

    def __init__(self, nome, preco):

        self.__id = None
        self.nome = nome
        self.preco = preco


    def __str__(self):

        return f'NOME: {self.nome} | PREÇO: {self.preco}'



    @property #Melhor para retorno mais seguro de "_preço"
    def preco(self):
        return self._preco


    @preco.setter #importante pra garantir de forma ideal a troca do "_preço"
    def preco(self, valor):

        try:
            valor = float(valor)
            self._preco = valor

        except ValueError as e:
            raise ValueError('Preço inválido')



    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, valor):

        if self.__id is None:
            self.__id = valor

        else:
            raise ValueError('ID já atribuído')


prod = Produto('arroz', 12.99)
print(prod)



id_gerado = data.insert(prod.nome, prod.preco)
prod.id = id_gerado

print(prod.id)