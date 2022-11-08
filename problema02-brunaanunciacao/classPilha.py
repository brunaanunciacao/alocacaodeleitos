class NoPilha:
    #iniciando o nó com o dado da pilha e a referencia para o nó anterior
    def __init__(self, dado=0):
        self.dado = dado
        self.no_anterior = None
    #função para retornar o dado do nó
    def __repr__(self):
        return str(self.dado)

class IdPilha:
    #iniciando um id para cada elemento inserido na pilha com referência ao id anterior
    def __init__(self, id = 0):
        self.id = id
        self.id_anterior = None
    #função para retornar o id
    def __repr__(self):
        return str(self.id)

class cPilha:
    #inicia a pilha com o topo e o id como None
    def __init__(self):
        self.__fim = None
        self.__id = None
        self.__NumObj = 0

    #insere o dado no topo da pilha e armazena o id do dado
    def inserir_pilha(self, n, id):
        novoNo = NoPilha(n)
        novoId = IdPilha(id)
        if self.__fim == None:
            self.__fim = novoNo
            self.__id = novoId
            self.__NumObj += 1
        else:
            novoNo.no_anterior = self.__fim
            self.__fim = novoNo
            novoId.id_anterior = self.__id
            self.__id = novoId
            self.__NumObj += 1

    #verifica se o topo é None se sim significa que a pilha está vazia
    def isVazia(self):
        if self.__fim is None:
            return True
        else:
            return False

    #remove o topo da pilha se não estiver vazia
    def remove_pilha(self):
        if self.__fim == None:
            return
        else:
            self.__fim = self.__fim.no_anterior
            self.__id = self.__id.id_anterior
            self.__NumObj -= 1

    #retorna o id do topo da pilha
    def retorneId(self):
        return self.__id

    #retorna o tamanho da pilha
    def tamanho(self):
        return self.__NumObj

    #função para retornar o dado da pilha
    def __repr__(self):
        return str(self.__fim)