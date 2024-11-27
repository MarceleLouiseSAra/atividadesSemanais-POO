import calendar
from interfaces import interfaceCalendario

class calendario(interfaceCalendario):
    def __init__(self, ano : int, inicio : int, fim : int) -> None:
        self.anoAtual = ano
        self.mesDeInicio = inicio
        self.mesEmQueAcaba = fim

    def criaListaDeListas(self) -> list: #cria uma lista de semanas dos meses do semestre
        calendario = calendar.Calendar()

        mesAux = self.mesEmQueAcaba + 13 - self.mesDeInicio
        mesAux += 1
        mes = self.mesDeInicio

        self.listaDeListas = []

        for i in range(1, mesAux):

            if mes > 12:
                mes = 1

            aux = calendario.monthdatescalendar(self.anoAtual, mes)
    
            aux = self.retiraDias(mes, aux) #chama a função que retira dias de meses que não estão no semestre

            self.listaDeListas += aux
            
            mes += 1

    def retiraDias(self, mes : int, aux : list) -> list: #como a .monthdatescalendar cria listas de semanas inteiras, faz-se necessário retirar dias de semanas que não estão no semestre

        listaAuxiliar = []

        for semana in aux:

            for dia in semana:
                if(dia.month != mes):
                    continue
                else:
                    listaAuxiliar.append(dia)

        return listaAuxiliar
