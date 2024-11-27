from interfaces import interfaceFeriados
import holidays

class feriados(interfaceFeriados):
    def __init__(self, ano : int, inicio : int, fim : int) -> None:
        self.anoAtual = ano
        self.mesDeInicio = inicio
        self.mesEmQueAcaba = fim

    def listaDeFeriados(self) -> list: # retorna uma lista com objetos datetime.date que são datas de feriados
        feriados = holidays.country_holidays("BR", subdiv="MG")

        inicio = str(self.anoAtual) + "-" + str(self.mesDeInicio) + "-" + "01"

        ano = self.anoAtual
        if self.mesDeInicio > self.mesEmQueAcaba:
            ano += 1

        fim = str(ano) + "-" + str(self.mesEmQueAcaba) + "-" + "31"

        feriadosDesteSemestre = feriados[inicio:fim]
        
        return feriadosDesteSemestre
    
    def removeFeriados(self, listaDeDias : list) -> list:
        feriadosDesteSemestre = self.listaDeFeriados()

        listaAuxiliar = []

        for dia in listaDeDias:
            controle = 1

            for feriado in feriadosDesteSemestre:
                if dia == feriado:
                    controle = 0
                    break
                else:
                    continue

            if controle:
                listaAuxiliar.append(dia)

        return listaAuxiliar

    def removeFinsDeSemana(self, listaDeDias : list) -> list:
        for dia in listaDeDias:
            if dia.strftime("%w") == "0": # remove da lista os domingos
                listaDeDias.remove(dia)

        for dia in listaDeDias:
            if dia.strftime("%w") == "6": # remove da lista os domingos
                listaDeDias.remove(dia)

        return listaDeDias