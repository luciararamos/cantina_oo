from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio


class Restaurante: #atributos e caracteristicas
    restaurantes = [] #variavel lista que ja adiciona 
    
    def __init__(self, nome, categoria):   #metodo construtor | parametros dentro do construtor |  #cada restaurante tem suas próprias informacoes com self, partes textuais
        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False #booleano    
        self._avaliacao = []
        self._cardapio = []

        Restaurante.restaurantes.append(self)  #append adiciona elementos a uma lista


    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    @classmethod #metodo de classe
    def listar_restaurantes(cls):
        print(f'{"Nome".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliacao".ljust(25)} | {"Ativo"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')


    @property #modificar atributo
    def ativo(self):
        return '☑' if self._ativo else '☐'


    def alternar_estado(self):
        self._ativo = not self._ativo


    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):  
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media


    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self.nome}\n')
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_tamanho'):
                mensagem = f'{i}. Nome: {item._nome} | Preço: R$ {item.preco:.2f} | Tamanho: {item._tamanho}'
                print(mensagem)
            else:
                mensagem = f'{i}. Nome: {item._nome} | Preço: R$ {item.preco:.2f} | Descrição: {item._descricao}'
                print(mensagem)