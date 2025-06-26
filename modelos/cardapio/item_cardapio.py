from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco  

    @abstractmethod
    def aplicar_desconto(self):
        pass

    @property
    def preco(self):
        return self._preco * 1.08