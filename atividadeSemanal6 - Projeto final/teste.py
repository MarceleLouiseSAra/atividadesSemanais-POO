import calendar 
import holidays

feriados = holidays.country_holidays("BR", subdiv="MG")
feriados_2semestre = feriados["2024-09-01":"2025-01-31"]

calendario = calendar.Calendar()

ano = 2024
mês = 9

listaDeDias = []
listaDeListas = []
aux = calendario.monthdatescalendar(ano, mês)

listaDeListas += aux

mês += 1
aux = calendario.monthdatescalendar(ano, mês)

listaDeListas += aux

print(listaDeListas)



for lista in listaDeListas:
    for dia in lista:

        if(dia.month != mês): # a .monthdatescalendar retorna listas com semanas inteiras; essa linha retira os dias de meses que não são o especificado
            continue

        controle = 1
        for feriado in feriados_2semestre:
            if dia == feriado:
                controle = 0
                continue
            else:
                controle = 1
                continue
        if controle: # caso o dia não for um feriado, ele é appendado à lista listaDeDias
            #print(dia)
            listaDeDias.append(dia)

for dia in listaDeDias:
    if dia.strftime("%w") == "0": # remove da lista os domingos
        listaDeDias.remove(dia)

for dia in listaDeDias:
    if dia.strftime("%w") == "6": # remove da lista os sábados
        listaDeDias.remove(dia)

print(len(listaDeDias)) # número de dias úteis em setembro
