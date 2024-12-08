def verificaEntradaNumérica():
    
    while True:

        try:
            entradaNumerica = int(input())
        except (ValueError, TypeError):
            print("\nO tipo da entrada dada é inesperado: forneça uma entrada válida.")
        except Exception as erro:
            print(f"\nFoi encontrado um {erro.__class__}. Forneça uma entrada válida.")
        else:
            if entradaNumerica < 0:
                print("\nEntrada negativa: forneça uma entrada válida.")
            else:
                return entradaNumerica 

def verificaEntradaAlfabetica():
    
    while True:
        
        entradaAlfabetica = input("escreva")

        if not(entradaAlfabetica.isalpha()):
            
            for caractere in range(len(entradaAlfabetica)):
                if entradaAlfabetica[caractere].isalpha() or entradaAlfabetica[caractere].isspace():
                    controle = 1
                    continue
                else: 
                    controle = 0
                    print("\nEntrada inválida: forneça uma nova entrada.")
                    break

        else:
            return entradaAlfabetica
        
        if controle:
            return entradaAlfabetica
        else:
            continue

import calendar
import holidays

def diasUteisDoSemestre():
    # feriados = holidays.country_holidays("BR")
    # feriadosDesteSemestre = feriados["2024-09-01":"2025-01-31"]

    # # print(feriadosDesteSemestre, end = "\n")

    # calendarioDesteAno = calendar.Calendar()

    # ano = 2024
    # mes = 9

    # calendarioDesteAno = calendarioDesteAno.monthdatescalendar(ano, mes)

    # # print(calendarioDesteAno, end = "\n")

    # listaDeListas = []
    # listaDeListas = calendarioDesteAno

    # # print(listaDeListas, end = "\n")

    # listaDeDias = []

    # for lista in listaDeListas:
    #     # print(lista, end = "\n")

    #     for dia in lista:
    #         # print(dia, end = "\n")

    #         if dia.month != mes:
    #             continue

    #         for feriado in feriadosDesteSemestre:
    #             if dia == feriado:
    #                 controle = 0
    #                 break
    #             else: 
    #                 controle = 1

    #         if controle:
    #             listaDeDias.append(dia)
    #         else:
    #             continue

    # for dia in listaDeDias:
    #     if dia.strftime("%w") == "0":
    #         listaDeDias.remove(dia)

    # for dia in listaDeDias:
    #     if dia.strftime("%w") == "6":
    #         listaDeDias.remove(dia)

    # print(listaDeDias, end = "\n")

    # print(len(listaDeDias), end = "\n")

    feriados = holidays.country_holidays("BR")
    feriadosDesteSemestre = feriados["2024-09-01":"2025-01-31"]

    # print(feriadosDesteSemestre)

    ano = 2024
    mes = 9

    calendarioDesteAno = calendar.Calendar()
    listaDeListas = []
    listaDeListas = calendarioDesteAno.monthdatescalendar(ano, mes)

    # print(listaDeListas)

    listaDeDias = []

    for lista in listaDeListas:
        # print(lista, end = "\n")

        for dia in lista:
            # print(dia, end = "\n")

            if dia.month != mes:
                continue

            for feriado in feriadosDesteSemestre:
                if dia == feriado:
                    controle = 0
                    break
                else:
                    controle = 1

            if controle:
                listaDeDias.append(dia)
            else:
                continue

    for dia in listaDeDias:
        if dia.strftime("%w") == "0":
            listaDeDias.remove(dia)

    for dia in listaDeDias:
        if dia.strftime("%w") == "6":
            listaDeDias.remove(dia)

    print(listaDeDias)

    print(len(listaDeDias))

def escreverArquivo(entrada):
    with open("arquivo.txt", "w") as arquivo:
        arquivo.write(entrada)

def appendarArquivo():
    with open("arquivo.txt", "a") as arquivo:
        arquivo.write("escrevi aqui\n")

def lerArquivo():
    with open("arquivo.txt", "r") as arquivo:
        arquivoLido = []
        for linha in  arquivo:
            arquivoLido.append(linha)

    return arquivoLido

def main():

    # print(verificaEntradaNumérica())

    # print(verificaEntradaAlfabetica())

    # diasUteisDoSemestre()

    escreverArquivo(verificaEntradaAlfabetica()) # tchubirau

    escreverArquivo(verificaEntradaAlfabetica()) # down down

    appendarArquivo()

    appendarArquivo() # down downescrevi aqui
                      # escrevi aqui

    print(lerArquivo()) # ['down downescrevi aqui\n', 'escrevi aqui\n']

main()