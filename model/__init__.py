

class Produto:

    def __init__(self, nome, preco):

        self.__id = None
        self.nome = nome
        self.preco = preco


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