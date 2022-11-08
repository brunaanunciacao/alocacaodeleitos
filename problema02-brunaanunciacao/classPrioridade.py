class NoPrioridade:
    #inicializa um nó baseado no dado, sua prioridade e a referencia para o próximo dado
    def __init__(self, dado, prioridade):
        self.dado = dado
        self.prioridade = prioridade
        self.prox = None

class FilaPrioridade:
    #inicia a fila sem nenhum elemento
    def __init__(self):
        self.__inicio = None

    #função para verificar se a fila está vazia
    def isVazia(self):
        if self.__inicio == None:
            return True
        else:
            return False

    #verifica primeiro se a fila está vazia, se estiver define o primeiro dado como o NoPrioridade
    def insert(self, valor, prioridade):
        if self.isVazia() == True:
            self.__inicio = NoPrioridade(valor, prioridade)
            return 1
        else:
        #senão, verifica se a prioridade do inicio é maior que a prioridade do dado a inserir
        #se for, o dado é adicionado em primeiro lugar e o dado anterior passa a ser o proximo do dado inserido
            if self.__inicio.prioridade > prioridade:
                novoNo = NoPrioridade(valor, prioridade)
                novoNo.prox = self.__inicio
                self.__inicio = novoNo
                return 1
        #se não for, é definida uma variavel auxiliar que recebe o valor do inicio da fila e enquanto houver proximo dessa variavel
        #irá verificar a condição da prioridade do novo dado com a prioridade do proximo da auxiliar
            else:
                aux = self.__inicio
                while aux.prox:
                    if prioridade <= aux.prox.prioridade:
                        break
                    aux = aux.prox
                novoNo = NoPrioridade(valor, prioridade)
                novoNo.prox = aux.prox
                aux.prox = novoNo
                return 1

    #verifica se a fila esta vazia
    def delete_FP(self):
        if self.isVazia() == True:
            return
    #senão o inicio da fila é redirecionado para o próximo elemento da ordem
        else:
            self.__inicio = self.__inicio.prox
            return 1

    #retorna o primeiro da fila se ela não estiver vazia
    def maior(self):
        if self.isVazia() == True:
            return
        else:
            return self.__inicio.dado



