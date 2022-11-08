import classPilha
import classElemento
import classPrioridade
import random

#classe para alterar as cores nos prints
class bcolors:
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    lightgrey = '\033[37m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    cyan = '\033[36m'
    purple = '\033[35m'
    pink = '\033[95m'
    ENDC = '\033[0m'

    def disable(self):
        self.ENDC = ''

#função para sortear se o paciente irá alterar de estado de saúde ou não
def sorteio(probabilidade):
    #probabilidade do paciente piorar seu estado de saúde
    if probabilidade <= 15:
        return 1
    #probabilidade do paciente melhorar seu estado de saúde
    if probabilidade > 15 and probabilidade <= 30:
        return 2
    #probabilidade do paciente se manter estável
    if probabilidade > 30:
        return 0

if __name__ == '__main__':
    #filas de prioridade:
    neonatal = classPrioridade.FilaPrioridade()
    pediatria = classPrioridade.FilaPrioridade()
    adulto = classPrioridade.FilaPrioridade()

    #pilhas de leitos:
    leito_neo = classPilha.cPilha()
    leito_pedi = classPilha.cPilha()
    leito_adul = classPilha.cPilha()
    #for para definir quantos ciclos o programa irá rodar
    for dia in range(5):
        print("-------------------------------------------------")
        print("")
        print(bcolors.purple, " <- Dia", dia + 1, "->", bcolors.ENDC)
        print("")

        #for para gerar uma quantidade aleatória de leitos
        for i in range(random.randint(5, 10)):
            #número do leito, hospital de origem e tipo do leito são gerados aleatoriamente
            leitos = classElemento.Elemento(random.randint(1, 99), chr(random.randint(65, 69)), random.randint(1, 3))
            #se o tipo do leito for 1- Neonatal, o número do leito e o hospital é armazenado na pilha neonatal
            if leitos.tipo == 1:
                leito_neo.inserir_pilha(leitos.numero, leitos.id)
            #se o tipo do leito for 2- Pediátrico, o número do leito e o hospital é armazenado na pilha pediatrica
            if leitos.tipo == 2:
                leito_pedi.inserir_pilha(leitos.numero, leitos.id)
            #se o tipo do leito for 3- Adulto, o número do leito e o hospital é armazenado na pilha adulto
            if leitos.tipo == 3:
                leito_adul.inserir_pilha(leitos.numero, leitos.id)

        #for para gerar aleatoriamente a quantidade de pacientes
        for i in range(random.randint(1, 15)):
            #número de paciente, gravidade e idade são gerados aleatoriamente
            paciente = classElemento.Elemento(random.randint(1000000, 9999999), random.randint(1, 5), random.randint(1, 3))
            #probabilidade para gerar o estado do paciente
            melhora_ou_piora = random.randint(0, 100)
            #armazena o retorno da função sorteio
            resultado = sorteio(melhora_ou_piora)
            print("-------------------------------------------------")

            #print dos pacientes, exibindo o número, gravidade e idades
            if paciente.tipo == 1:
                if paciente.id == 1:
                    print("Paciente:", paciente.numero, bcolors.red, "[Emergência]", bcolors.ENDC, bcolors.cyan,"[Neonatal]", bcolors.ENDC)
                elif paciente.id == 2:
                    print("Paciente:", paciente.numero, bcolors.orange, "[Muito Urgente]", bcolors.ENDC, bcolors.cyan,"[Neonatal]", bcolors.ENDC)
                elif paciente.id == 3:
                    print("Paciente:", paciente.numero, bcolors.yellow, "[Urgente]", bcolors.ENDC, bcolors.cyan,"[Neonatal]", bcolors.ENDC)
                elif paciente.id == 4:
                    print("Paciente:", paciente.numero, bcolors.lightgreen, "[Pouco Urgente]", bcolors.ENDC, bcolors.cyan,"[Neonatal]", bcolors.ENDC)
                else:
                    print("Paciente:", paciente.numero, bcolors.lightblue, "[Não Urgente]", bcolors.ENDC, bcolors.cyan,"[Neonatal]", bcolors.ENDC)
            elif paciente.tipo == 2:
                if paciente.id == 1:
                    print("Paciente:", paciente.numero, bcolors.red, "[Emergência]", bcolors.ENDC, bcolors.pink, "[Pediátrico]", bcolors.ENDC)
                elif paciente.id == 2:
                    print("Paciente:", paciente.numero, bcolors.orange, "[Muito Urgente]", bcolors.ENDC, bcolors.pink, "[Pediátrico]", bcolors.ENDC)
                elif paciente.id == 3:
                    print("Paciente:", paciente.numero, bcolors.yellow, "[Urgente]", bcolors.ENDC, bcolors.pink, "[Pediátrico]", bcolors.ENDC)
                elif paciente.id == 4:
                    print("Paciente:", paciente.numero, bcolors.lightgreen, "[Pouco Urgente]", bcolors.ENDC, bcolors.pink, "[Pediátrico]", bcolors.ENDC)
                else:
                    print("Paciente:", paciente.numero, bcolors.lightblue, "[Não Urgente]", bcolors.ENDC, bcolors.pink, "[Pediátrico]", bcolors.ENDC)
            else:
                if paciente.id == 1:
                    print("Paciente:", paciente.numero, bcolors.red, "[Emergência]", bcolors.ENDC, bcolors.lightgrey, "[Adulto]", bcolors.ENDC)
                elif paciente.id == 2:
                    print("Paciente:", paciente.numero, bcolors.orange, "[Muito Urgente]", bcolors.ENDC, bcolors.lightgrey, "[Adulto]", bcolors.ENDC)
                elif paciente.id == 3:
                    print("Paciente:", paciente.numero, bcolors.yellow, "[Urgente]", bcolors.ENDC, bcolors.lightgrey, "[Adulto]", bcolors.ENDC)
                elif paciente.id == 4:
                    print("Paciente:", paciente.numero, bcolors.lightgreen, "[Pouco Urgente]", bcolors.ENDC, bcolors.lightgrey, "[Adulto]", bcolors.ENDC)
                else:
                    print("Paciente:", paciente.numero, bcolors.lightblue, "[Não Urgente]", bcolors.ENDC, bcolors.lightgrey, "[Adulto]", bcolors.ENDC)

            #condição para o estado do paciente
            if resultado == 1:
            #se for 1 significa que o paciente piorou de estado e seu id é atualizado para o mais grave
                paciente.atualiza_id(paciente.id - 1)
                print(bcolors.lightred, "Paciente:", paciente.numero, "piorou na fila de espera", bcolors.ENDC)
            elif resultado == 2:
            #se for 2 significa que o paciente melhorou de estado e seu id é atualizado para o mais leve
                paciente.atualiza_id(paciente.id + 1)
                print(bcolors.cyan, "Paciente:", paciente.numero, "melhorou na fila de espera", bcolors.ENDC)
            else:
            #se não for nenhuma das 2 opções acima significa que o paciente se manteve estável durante a fila de espera
                pass
            print("-------------------------------------------------")

            #condição para os casos de pacientes que necessitam de UTI (ids 1, 2 e 3)
            if paciente.id >= 1 and paciente.id < 4:
            #se for 1, ele é inserido na fila de prioridade neonatal
                if paciente.tipo == 1:
                    neonatal.insert(paciente.numero, paciente.id)
            #se for 2, ele é inserido na fila de prioridade pediatria
                if paciente.tipo == 2:
                    pediatria.insert(paciente.numero, paciente.id)
            #se for 3, ele é inserido na fila de prioridade adulto
                if paciente.tipo == 3:
                    adulto.insert(paciente.numero, paciente.id)
        print("-------------------------------------------------")
        print(bcolors.cyan, "Leitos Neonatal disponíveis: ", bcolors.ENDC, leito_neo.tamanho() - 1)
        print("")
        print("Alocando pacientes neonatal aos leitos...")
        #enquanto o tamanho dos leitos for maior que 0 e a fila neonatal não estiver vazia
        #o paciente é alocado ao leito e retirado do sistema
        while leito_neo.tamanho() - 1 > 0:
            if neonatal.isVazia() is False:
                IdN = leito_neo.retorneId()
                leitosN_Ocupados = (neonatal.maior(), leito_neo)
                neonatal.delete_FP()
                leito_neo.remove_pilha()
            else:
                print("Não há pacientes neonatais na fila.")
                break
            print("| Paciente:", str(leitosN_Ocupados[0]), "| Leito do Hospital:", IdN, "| Número:", str(leitosN_Ocupados[1]), "|")
        if leito_neo.tamanho() - 1  == 0:
            print("")
            print("Não há leitos disponíveis, aguarde a liberação.")
        print("-------------------------------------------------")
        print(bcolors.pink, "Leitos Pediátricos disponíveis: ", bcolors.ENDC, leito_pedi.tamanho() - 1)
        print("")
        print("Alocando pacientes pediátricos aos leitos...")
        #enquanto o tamanho dos leitos for maior que 0 e a fila pediátrico não estiver vazia
        #o paciente é alocado ao leito e retirado do sistema
        while leito_pedi.tamanho() - 1 > 0:
            if pediatria.isVazia() is False:
                IdP = leito_pedi.retorneId()
                leitosP_Ocupados = (pediatria.maior(), leito_pedi)
                pediatria.delete_FP()
                leito_pedi.remove_pilha()
            else:
                print("Não há pacientes pediátricos na fila.")
                break
            print("| Paciente:", str(leitosP_Ocupados[0]), "| Leito do Hospital:", IdP, "| Número:", str(leitosP_Ocupados[1]), "|")
        if leito_pedi.tamanho() - 1 == 0:
            print("")
            print("Não há leitos disponíveis, aguarde a liberação.")
        print("-------------------------------------------------")
        print(bcolors.lightgrey, "Leitos Adulto disponíveis: ", bcolors.ENDC, leito_adul.tamanho() - 1)
        print("")
        print("Alocando pacientes adultos aos leitos...")
        #enquanto o tamanho dos leitos for maior que 0 e a fila adulto não estiver vazia
        #o paciente é alocado ao leito e retirado do sistema
        while leito_adul.tamanho() - 1  > 0:
            if adulto.isVazia() is False:
                IdA = leito_adul.retorneId()
                leitosA_Ocupados = (adulto.maior(), leito_adul)
                adulto.delete_FP()
                leito_adul.remove_pilha()
            else:
                print("Não há pacientes adultos na fila.")
                break
            print("| Paciente:", str(leitosA_Ocupados[0]), "| Leito do Hospital:", IdA, "| Número:", str(leitosA_Ocupados[1]), "|")
        if leito_adul.tamanho() - 1 == 0:
            print("")
            print("Não há leitos disponíveis, aguarde a liberação.")
        print("-------------------------------------------------")