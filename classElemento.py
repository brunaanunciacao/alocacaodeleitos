#classe para definir as tuplas que são usadas na identificação dos pacientes
class Elemento:
    #iniciando com o número de identificação, nível de urgência e a idade do paciente
    #nível de urgência:  1- Emergência  2- Muito Urgente  3- Urgente  4- Pouco Urgente  5- Não Urgente
    #idade do paciente:  1- Neonatal (0 - 11 meses)  2- Pediátrico (1 - 13 anos)  3- Adulto (Acima de 13 anos)
    def __init__(self, numero, id, tipo):
        self.numero = numero
        self.id = id
        self.tipo = tipo
        self.Identificador = [self.numero, self.id, self.tipo]

    #retorna os dados do paciente como uma tupla
    def retorne(self):
        return self.Identificador

    #retorna apenas o número de identificação
    def retorne_numero(self):
        return self.Identificador[0]

    #retorna apenas o nível de urgência
    def retorne_id(self):
        return self.Identificador[1]

    #retorna apenas a idade do paciente
    def retorne_tipo(self):
        return self.Identificador[2]

    #troca o id do paciente em caso de melhora ou piora do caso
    def atualiza_id(self, id):
        self.id = id
        self.Identificador = [self.numero, id, self.tipo]

    #função para formatar a saída dos dados
    def __str__(self):
        outStr = ""
        outStr += f'{self.Identificador[0]}\n'
        outStr += f'{self.Identificador[1]}\n'
        outStr += f'{self.Identificador[2]}\n'
        return outStr







